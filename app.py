from gentlecare import app 
import distro
distro.linux_distribution()

if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5001)
    