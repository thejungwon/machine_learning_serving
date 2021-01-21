import requests



def download():
    url = 'https://s3.amazonaws.com/img-datasets/mnist.npz'
    r = requests.get(url, allow_redirects=True)
    open('mnist.npz', 'wb').write(r.content)    



if __name__ == "__main__":
    download()