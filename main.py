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


##installing go language

def go_install():
	go = subprocess.run(['go version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if go.returncode != 0:
		print("Go is Not Installed")
		print("Installing Go")
		subprocess.run(['apt-get -y install golang',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		go1 = subprocess.run(['go version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if go1.returncode == 0:
			print("\033[32mGo is installed")
		else:
			print("Failled to Install go")
	else:
		print("\033[32mGo is installed")

##installing gcc

def gcc_install():
	gcc = subprocess.run(['gcc -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if gcc.returncode != 0:
		print("gcc is Not Installed")
		print("Installing gcc")
		subprocess.run(['apt -y install build-essential',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['apt-get -y install manpages-dev',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gcc1 = subprocess.run(['gcc -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gcc1.returncode == 0:
			print("\033[32mgcc is installed")
		else:
			print("Failled to Install gcc")
	else:
		print("\033[32mgcc is installed")

##installing make

def make_install():
	make = subprocess.run(['make -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if make.returncode != 0:
		print("make is Not Installed")
		print("Installing Make")
		subprocess.run(['apt-get -y install make',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		make1 = subprocess.run(['make -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if make1.returncode == 0:
			print("\033[32mmake is installed")
		else:
			print("Failled to Install make")
	else:
		print("\033[32mmake is installed")


##installing dig

def dig_install():
	dig = subprocess.run(['dig -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if dig.returncode != 0:
		print("Dig is Not Installed")
		print("Installing Dig")
		subprocess.run(['apt-get -y install dnsutils',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		dig1 = subprocess.run(['dig -v',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if dig1.returncode == 0:
			print("\033[32mDig is installed")
		else:
			print("Failled to Install Dig")
	else:
		print("\033[32mDig is installed")


##installing dnsx

def dnsx_install():
	dnsx = subprocess.run(['dnsx',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if dnsx.returncode != 0:
		print("Dnsx is Not Installed")
		print("Installing Dnsx")
		subprocess.run(['GO111MODULE=on go get -v github.com/projectdiscovery/dnsx/cmd/dnsx',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/dnsx /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		dnsx1 = subprocess.run(['dnsx',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


		if dnsx1.returncode == 0:
			print("\033[32mDnsx is installed")
		else:
			print("Failled to Install Dnsx")
	else:
		print("\033[32mDnsx is installed")


##installing subfinder

def subfinder_install():
	finder = subprocess.run(['subfinder -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if finder.returncode != 0:
		print("Subfinder is Not Installed")
		print("Installing Subfinder")
		subprocess.run(['GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/subfinder /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		inder = subprocess.run(['subfinder -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if inder.returncode == 0:
			print("\033[32mSubfinder is installed")
		else:
			print("Failled to Install Subfinder")
	else:
		print("\033[32mSubfinder is installed")

##installing nuclei


def nuclei_install():
	nuclei = subprocess.run(['nuclei -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if nuclei.returncode != 0:
		print("Nuclei is Not Installed")
		print("Installing Nuclei")
		subprocess.run(['GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/nuclei /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		nuclei1 = subprocess.run(['nuclei -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if nuclei1.returncode == 0:
			print("\033[32mNuclei is installed")
		else:
			print("Failled to Install Nuclei")
	else:
		print("\033[32mNuclei is installed")

##installing assetfinder

def assetfinder_install():
	asset = subprocess.run(['assetfinder -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if asset.returncode != 0:
		print("Assetfinder is Not Installed")
		print("Installing Assetfinder")
		subprocess.run(['go get -u github.com/tomnomnom/assetfinder',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/assetfinder /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		asset = subprocess.run(['assetfinder -d',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if asset.returncode == 0:
			print("\033[32mAssetfinder is installed")
		else:
			print("Failled to Install Asssefinder")
	else:
		print("\033[32mAssetfinder is installed")


##installing jq

def jq_install():
	jq = subprocess.run(['jq --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if jq.returncode != 0:
		print("jq is Not Installed")
		print("Installing jq")
		subprocess.run(['apt-get install jq -y',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		jq1 = subprocess.run(['jq --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if jq1.returncode == 0:
			print("\033[32mjq is installed")
		else:
			print("Failled to Install jq")
	else:
		print("\033[32mjq is installed")


##installing httprobe

def httprobe_install():
	probe = subprocess.run(['httprobe -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if probe.returncode != 0:
		print("Httprobe is Not Installed")
		print("Installing Httprobe")
		subprocess.run(['go get -u github.com/tomnomnom/httprobe',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/httprobe /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		probe1 = subprocess.run(['httprobe -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if probe1.returncode == 0:
			print("\033[32mHttprobe is installed")
		else:
			print("Failled to Install Httprobe")
	else:
		print("\033[32mHttprobe is installed")

##installing waybackurl


def waybackurl_install():
	url = subprocess.run(['waybackurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if url.returncode != 0:
		print("Waybackurls is Not Installed")
		print("Installing Waybackurls")
		subprocess.run(['go get github.com/tomnomnom/waybackurls',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/waybackurls /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		url1 = subprocess.run(['waybackurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if url1.returncode == 0:
			print("\033[32mWaybackurls is installed")
		else:
			print("Failled to Install Waybackurls")
	else:
		print("\033[32mWaybackurls is installed")


##installing meg

def meg_install():
	meg = subprocess.run(['meg -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if meg.returncode != 0:
		print("Meg is Not Installed")
		print("Installing Meg")
		subprocess.run(['go get -u github.com/tomnomnom/meg',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/meg /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		meg1 = subprocess.run(['meg -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if meg1.returncode == 0:
			print("\033[32mMeg is installed")
		else:
			print("Failled to Install Meg")
	else:
		print("\033[32mMeg is installed")

##installing gf


def gf_install():
	gf = subprocess.run(['gf --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if gf.returncode != 0:
		print("gf is Not Installed")
		print("Installing gf")
		subprocess.run(['go get -u github.com/tomnomnom/gf',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/gf /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gf = subprocess.run(['gf --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if gf.returncode == 0:
			print("\033[32mgf is installed")
		else:
			print("Failled to Install gf")
	else:
		print("\033[32mgf is installed")

##installing gron


def gron_install():
	gron = subprocess.run(['gron -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if gron.returncode != 0:
		print("Gron is Not Installed")
		print("Installing Gron")
		subprocess.run(['go get -u github.com/tomnomnom/gron',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/gron /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gron1 = subprocess.run(['gron -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if gron1.returncode == 0:
			print("\033[32mGron is installed")
		else:
			print("Failled to Install Gron")
	else:
		print("\033[32mGron is installed")


##installing webscreenshot

def webscreenshot_install():
	shoot = subprocess.run(['webscreenshot -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if shoot.returncode != 0:
		print("webscreenshot is Not Installed")
		print("Installing webscreenshot")
		subprocess.run(['pip install webscreenshot',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['pip install selenium',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		shoot1 = subprocess.run(['webscreenshot -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if shoot1.returncode == 0:
			print("\033[32mwebscreenshot is installed")
		else:
			print("Failled to Install webscreenshot")
	else:
		print("\033[32mwebscreenshot is installed")


##installing waybackunifier

def waybackunifier_install():
	backfin = subprocess.run(['waybackunifier -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if backfin.returncode != 0:
		print("waybackunifier is Not Installed")
		print("Installing waybackunifier")
		subprocess.run(['go get github.com/mhmdiaa/waybackunifier',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/waybackunifier /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		backfin1 = subprocess.run(['waybackunifier -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if backfin1.returncode == 0:
			print("\033[32mwaybackunifier is installed")
		else:
			print("Failled to Install waybackunifier")
	else:
		print("\033[32mwaybackunifier is installed")


##installing shodan

def shodan_install():
	shodan = subprocess.run(['shodan -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if shodan.returncode != 0:
		print("shodan is Not Installed")
		print("Installing shodan")
		subprocess.run(['pip3 install shodan',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		shodan1 = subprocess.run(['shodan -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if shodan1.returncode == 0:
			print("\033[32mshodan is installed")
		else:
			print("Failled to Install shodan")
	else:
		print("\033[32mshodan is installed")

##installing censys

def censys_install():
	cen = subprocess.run(['censys',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if cen.returncode != 0:
		print("censys is Not Installed")
		print("Installing censys")
		subprocess.run(['pip3 install censys',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		cen1 = subprocess.run(['censys',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if cen1.returncode == 0:
			print("\033[32mcensys is installed")
		else:
			print("Failled to Install censys")
	else:
		print("\033[32mcensys is installed")


##installing goaltdns

def goaltdns_install():
	goaltdns = subprocess.run(['goaltdns --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if goaltdns.returncode != 0:
		print("goaltdns is Not Installed")
		print("Installing goaltdns")
		subprocess.run(['go get github.com/subfinder/goaltdns',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/goaltdns /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		goaltdns1 = subprocess.run(['goaltdns --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if goaltdns1.returncode == 0:
			print("\033[32mgoaltdns is installed")
		else:
			print("Failled to Install goaltdns")
	else:
		print("\033[32mgoaltdns is installed")

##installing subjack


def subjack_install():
	subjack= subprocess.run(['subjack -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if subjack.returncode != 0:
		print("subjack is Not Installed")
		print("Installing subjack")
		subprocess.run(['go get github.com/haccer/subjack',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/subjack /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subjack1= subprocess.run(['subjack -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if subjack1.returncode == 0:
			print("\033[32msubjack is installed")
		else:
			print("Failled to Install subjack")
	else:
		print("\033[32msubjack is installed")

##installing ffuf


def ffuf_install():
	ffuf= subprocess.run(['ffuf --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if ffuf.returncode != 0:
		print("FFUF is Not Installed")
		print("Installing FFUF")
		subprocess.run(['go get -u github.com/ffuf/ffuf',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/ffuf /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		ffuf1= subprocess.run(['ffuf --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


		if ffuf1.returncode == 0:
			print("\033[32mFFUF is installed")
		else:
			print("Failled to Install FFUF")
	else:
		print("\033[32mFFUF is installed")


##installing hakrawler

def hawk_install():
	hawk= subprocess.run(['hakrawler -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if hawk.returncode != 0:
		print("hakrawler is Not Installed")
		print("Installing hakrawler")
		subprocess.run(['go get github.com/hakluke/hakrawler',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/hakrawler /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		hawk1= subprocess.run(['hakrawler -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if hawk1.returncode == 2:
			print("\033[32mhakrawler is installed")
		else:
			print("Failled to Install hakrawler")
	else:
		print("\033[32mhakrawler is installed")


##installing kxss

def kxss_install():
		subprocess.run(['go get github.com/Emoe/kxss',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/kxss /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("\033[32mKxss is installed")


##installing otxurls

def otxurls_install():
	otxurls= subprocess.run(['otxurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if otxurls.returncode != 0:
		print("otxurls is Not Installed")
		print("Installing otxurls")
		subprocess.run(['go get github.com/lc/otxurls',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/otxurls /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		otxurls1= subprocess.run(['otxurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if otxurls1.returncode == 0:
			print("\033[32motxurls is installed")
		else:
			print("Failled to Install otxurls")
	else:
		print("\033[32motxurls is installed")


##installing dalfox

def dalfox_install():
		subprocess.run(['sudo apt install snapd -y',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['sudo snap install dalfox',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("\033[32motxurls is installed")


##installing subjs

def subjs_install():
	subjs= subprocess.run(['subjs -version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if subjs.returncode != 0:
		print("subjs is Not Installed")
		print("Installing subjs")
		subprocess.run(['GO111MODULE=on go get -u -v github.com/lc/subjs',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/subjs /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subjs1= subprocess.run(['subjs -version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if subjs1.returncode == 0:
			print("\033[32msubjs is installed")
		else:
			print("Failled to Install subjs")
	else:
		print("\033[32msubjs is installed")

##installing gau


def gau_install():

		subprocess.run(['GO111MODULE=on go get -u -v github.com/lc/gau',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp /root/go/bin/gau /usr/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("\033[32mgau is installed")


##installing arjun

def arjun_install():
	gau= subprocess.run(['arjun -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if gau.returncode != 0:
		print("arjun is Not Installed")
		print("Installing arjun")
		subprocess.run(['pip3 install arjun',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gau1= subprocess.run(['arjun -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gau1.returncode == 0:
			print("\033[32marjun is installed")
		else:
			print("Failled to Install arjun")
	else:
		print("\033[32marjun is installed")





if __name__ == "__main__":
	
	go_install()
	gcc_install()
	make_install()
	dig_install()
	dnsx_install()
	subfinder_install()
	nuclei_install()
	assetfinder_install()
	jq_install()
	httprobe_install()
	waybackurl_install()
	meg_install()
	gf_install()
	gron_install()
	waybackunifier_install()
	shodan_install()
	censys_install()
	goaltdns_install()
	subjack_install()
	ffuf_install()
	hawk_install()
	kxss_install()
	otxurls_install()
	dalfox_install()
	subjs_install()
	gau_install()
	arjun_install()
	webscreenshot_install()




