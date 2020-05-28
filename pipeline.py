# wget https://www.fs.usda.gov/rds/archive/products/RDS-2005-0004/RDS-2005-0004.zip
# unzip RDS-2005-0004.zip
import conducto as co


def download_and_plot() -> co.Serial:
    download_command = """
            apt update -y && apt install -y curl unzip
            curl https://www.fs.usda.gov/rds/archive/products/RDS-2005-0004/RDS-2005-0004.zip > data.zip
            unzip data.zip
        """
    image = co.Image(dockerfile='./Dockerfile', context='.')
    with co.Serial(image=image) as pipeline:
        co.Exec(download_command, name="download")
        with co.Parallel(name='plot'):
            co.Exec('python rainfall.py', name='daily')
            co.Exec('python rainfall.py --resample M --save', name='monthly')
    return pipeline


if __name__ == '__main__':
    co.main(default=download_and_plot)
