from gentlecare import app 
import distro
distro.linux_distribution()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    