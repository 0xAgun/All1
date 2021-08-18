import subprocess
import sys
import time

banner = '''


 						\033[31;1m _______ __ __ _____ 
 						\033[31;1m|   _   |  |  | _   |
 						\033[31;1m|.  1   |  |  |.|   |
 						\033[31;1m|.  _   |__|__`-|.  |
 						\033[31;1m|:  |   |       |:  |
 						\033[31;1m|::.|:. |       |::.|
 						\033[31;1m`--- ---'       `---'\033[0m \033[32;1m[1.0.8]\033[0m
 						\033[34;1m[by 0xAgun]\033[0m
                      


'''



for char in banner:
	sys.stdout.write(char)
	sys.stdout.flush()
	time.sleep(0.01)
pass



def go_install():
	go = subprocess.Popen(['go version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	go.wait()

	if go.returncode != 0:
		print("Go is Not Installed")
		print("Installing Go")
		subprocess.Popen(['apt-get -y install golang',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if go.returncode == 0:
			pass
		else:
			print("Failled to Install go")
	else:
		print("\033[32mGo is installed")

go_install()

def gcc_install():
	gcc = subprocess.Popen(['gcc -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	gcc.wait()

	if gcc.returncode != 0:
		print("gcc is Not Installed")
		print("Installing gcc")
		subprocess.Popen(['apt -y install build-essential',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['apt-get -y install manpages-dev',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gcc.returncode == 0:
			pass
		else:
			print("Failled to Install gcc")
	else:
		print("\033[32mgcc is installed")

gcc_install()

def make_install():
	make = subprocess.Popen(['make -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	make.wait()

	if make.returncode != 0:
		print("make is Not Installed")
		print("Installing Make")
		subprocess.Popen(['apt-get -y install make',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if make.returncode == 0:
			pass
		else:
			print("Failled to Install make")
	else:
		print("\033[32mmake is installed")

make_install()

def dig_install():
	dig = subprocess.Popen(['dig -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	dig.wait()

	if dig.returncode != 0:
		print("Dig is Not Installed")
		print("Installing Dig")
		subprocess.Popen(['apt-get -y install dnsutils',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if dig.returncode == 0:
			pass
		else:
			print("Failled to Install Dig")
	else:
		print("\033[32mDig is installed")

dig_install()

def dnsx_install():
	dnsx = subprocess.Popen(['dnsx',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	dnsx.wait()

	if dnsx.returncode != 0:
		print("Dnsx is Not Installed")
		print("Installing Dnsx")
		subprocess.Popen(['GO111MODULE=on go get -v github.com/projectdiscovery/dnsx/cmd/dnsx',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/dnsx /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if dnsx.returncode == 0:
			pass
		else:
			print("Failled to Install Dnsx")
	else:
		print("\033[32mDnsx is installed")

dnsx_install()

def subfinder_install():
	finder = subprocess.Popen(['subfinder',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	finder.wait()

	if finder.returncode != 1:
		print("Subfinder is Not Installed")
		print("Installing Subfinder")
		subprocess.Popen(['GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/subfinder /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if finder.returncode == 1:
			pass
		else:
			print("Failled to Install Subfinder")
	else:
		print("\033[32mSubfinder is installed")

subfinder_install()

def nuclei_install():
	nuclei = subprocess.Popen(['nuclei -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	nuclei.wait()

	if nuclei.returncode != 0:
		print("Nuclei is Not Installed")
		print("Installing Nuclei")
		subprocess.Popen(['GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/nuclei /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if nuclei.returncode == 0:
			pass
		else:
			print("Failled to Install Nuclei")
	else:
		print("\033[32mNuclei is installed")

nuclei_install()

def assetfinder_install():
	asset = subprocess.Popen(['assetfinder -d',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	asset.wait()

	if asset.returncode != 2:
		print("Assetfinder is Not Installed")
		print("Installing Assetfinder")
		subprocess.Popen(['go get -u github.com/tomnomnom/assetfinder',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/assetfinder /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if asset.returncode == 1:
			pass
		else:
			print("Failled to Install Asssefinder")
	else:
		print("\033[32mAssetfinder is installed")

assetfinder_install()

def jq_install():
	jq = subprocess.Popen(['jq --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	jq.wait()

	if jq.returncode != 0:
		print("jq is Not Installed")
		print("Installing jq")
		subprocess.Popen(['apt-get install jq -y',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if jq.returncode == 0:
			pass
		else:
			print("Failled to Install jq")
	else:
		print("\033[32mjq is installed")

jq_install()

def httprobe_install():
	probe = subprocess.Popen(['httprobe -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	probe.wait()

	if probe.returncode != 0:
		print("Httprobe is Not Installed")
		print("Installing Httprobe")
		subprocess.Popen(['go get -u github.com/tomnomnom/httprobe',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/httprobe /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if probe.returncode == 0:
			pass
		else:
			print("Failled to Install Httprobe")
	else:
		print("\033[32mHttprobe is installed")

httprobe_install()

def waybackurl_install():
	url = subprocess.Popen(['waybackurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	url.wait()

	if url.returncode != 0:
		print("Waybackurls is Not Installed")
		print("Installing Waybackurls")
		subprocess.Popen(['go get github.com/tomnomnom/waybackurls',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/waybackurls /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if url.returncode == 0:
			pass
		else:
			print("Failled to Install Waybackurls")
	else:
		print("\033[32mWaybackurls is installed")

waybackurl_install()

def meg_install():
	meg = subprocess.Popen(['meg -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	meg.wait()

	if meg.returncode != 0:
		print("Meg is Not Installed")
		print("Installing Meg")
		subprocess.Popen(['go get -u github.com/tomnomnom/meg',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/meg /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if meg.returncode == 0:
			pass
		else:
			print("Failled to Install Meg")
	else:
		print("\033[32mMeg is installed")

meg_install()

def gf_install():
	gf = subprocess.Popen(['gf',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	gf.wait()

	if gf.returncode != 0:
		print("gf is Not Installed")
		print("Installing gf")
		subprocess.Popen(['go get -u github.com/tomnomnom/gf',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/gf /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if gf.returncode == 0:
			pass
		else:
			print("Failled to Install gf")
	else:
		print("\033[32mgf is installed")

gf_install()

def gron_install():
	gron = subprocess.Popen(['gron -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	gron.wait()

	if gron.returncode != 0:
		print("Gron is Not Installed")
		print("Installing Gron")
		subprocess.Popen(['go get -u github.com/tomnomnom/gron',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/gron /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if gron.returncode == 0:
			pass
		else:
			print("Failled to Install Gron")
	else:
		print("\033[32mGron is installed")

gron_install()

def webscreenshot_install():
	shoot = subprocess.Popen(['webscreenshot -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	shoot.wait()

	if shoot.returncode != 0:
		print("webscreenshot is Not Installed")
		print("Installing webscreenshot")
		subprocess.Popen(['pip install webscreenshot',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['pip install selenium',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if shoot.returncode == 0:
			pass
		else:
			print("Failled to Install webscreenshot")
	else:
		print("\033[32mwebscreenshot is installed")

webscreenshot_install()

def waybackunifier_install():
	backfin = subprocess.Popen(['waybackunifier -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	backfin.wait()

	if backfin.returncode != 0:
		print("waybackunifier is Not Installed")
		print("Installing waybackunifier")
		subprocess.Popen(['go get github.com/mhmdiaa/waybackunifier',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/waybackunifier /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if backfin.returncode == 0:
			pass
		else:
			print("Failled to Install waybackunifier")
	else:
		print("\033[32mwaybackunifier is installed")

waybackunifier_install()

def shodan_install():
	shodan = subprocess.Popen(['shodan -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	shodan.wait()

	if shodan.returncode != 0:
		print("shodan is Not Installed")
		print("Installing shodan")
		subprocess.Popen(['pip3 install shodan',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if shodan.returncode == 0:
			pass
		else:
			print("Failled to Install shodan")
	else:
		print("\033[32mshodan is installed")

shodan_install()

def censys_install():
	cen = subprocess.Popen(['censys',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	cen.wait()

	if cen.returncode != 0:
		print("censys is Not Installed")
		print("Installing censys")
		subprocess.Popen(['pip3 install censys',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if cen.returncode == 0:
			pass
		else:
			print("Failled to Install censys")
	else:
		print("\033[32mcensys is installed")

censys_install()

def goaltdns_install():
	goaltdns = subprocess.Popen(['goaltdns --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	goaltdns.wait()

	if goaltdns.returncode != 0:
		print("goaltdns is Not Installed")
		print("Installing goaltdns")
		subprocess.Popen(['go get github.com/subfinder/goaltdns',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/goaltdns /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if goaltdns.returncode == 0:
			pass
		else:
			print("Failled to Install goaltdns")
	else:
		print("\033[32mgoaltdns is installed")

goaltdns_install()

def subjack_install():
	subjack= subprocess.Popen(['subjack -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	subjack.wait()

	if subjack.returncode != 0:
		print("subjack is Not Installed")
		print("Installing subjack")
		subprocess.Popen(['go get github.com/haccer/subjack',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/subjack /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if subjack.returncode == 0:
			pass
		else:
			print("Failled to Install subjack")
	else:
		print("\033[32msubjack is installed")

subjack_install()

def ffuf_install():
	ffuf= subprocess.Popen(['ffuf --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	ffuf.wait()

	if ffuf.returncode != 0:
		print("FFUF is Not Installed")
		print("Installing FFUF")
		subprocess.Popen(['go get -u github.com/ffuf/ffuf',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/ffuf /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if ffuf.returncode == 0:
			pass
		else:
			print("Failled to Install FFUF")
	else:
		print("\033[32mFFUF is installed")

ffuf_install()

def hawk_install():
	hawk= subprocess.Popen(['hakrawler -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	hawk.wait()

	if hawk.returncode != 2:
		print("hakrawler is Not Installed")
		print("Installing hakrawler")
		subprocess.Popen(['go get github.com/hakluke/hakrawler',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/hakrawler /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if hawk.returncode == 2:
			pass
		else:
			print("Failled to Install hakrawler")
	else:
		print("\033[32mhakrawler is installed")

hawk_install()

def kxss_install():
		subprocess.Popen(['go get github.com/Emoe/kxss',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/kxss /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("\033[32mKxss is installed")

kxss_install()

def otxurls_install():
	otxurls= subprocess.Popen(['otxurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	otxurls.wait()

	if otxurls.returncode != 0:
		print("otxurls is Not Installed")
		print("Installing otxurls")
		subprocess.Popen(['go get github.com/lc/otxurls',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/otxurls /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if otxurls.returncode == 0:
			pass
		else:
			print("Failled to Install otxurls")
	else:
		print("\033[32motxurls is installed")

otxurls_install()

def dalfox_install():
		subprocess.Popen(['sudo apt install snapd -y',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['sudo snap install dalfox',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("\033[32motxurls is installed")

dalfox_install()

def subjs_install():
	subjs= subprocess.Popen(['subjs -version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	subjs.wait()

	if subjs.returncode != 0:
		print("subjs is Not Installed")
		print("Installing subjs")
		subprocess.Popen(['GO111MODULE=on go get -u -v github.com/lc/subjs',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/subjs /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if subjs.returncode == 0:
			pass
		else:
			print("Failled to Install subjs")
	else:
		print("\033[32msubjs is installed")

subjs_install()

def gau_install():
	gau= subprocess.Popen(['subjs -version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	gau.wait()

	if gau.returncode != 0:
		print("gau is Not Installed")
		print("Installing gau")
		subprocess.Popen(['GO111MODULE=on go get -u -v github.com/lc/gau',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.Popen(['cp /root/go/bin/gau /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if gau.returncode == 0:
			pass
		else:
			print("Failled to Install gau")
	else:
		print("\033[32mgau is installed")

gau_install()


def arjun_install():
	gau= subprocess.Popen(['arjun -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	gau.wait()

	if gau.returncode != 0:
		print("arjun is Not Installed")
		print("Installing arjun")
		subprocess.Popen(['pip3 install arjun',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gau.returncode == 0:
			pass
		else:
			print("Failled to Install arjun")
	else:
		print("\033[32marjun is installed")

arjun_install()
