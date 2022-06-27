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
 						\033[31;1m`--- ---'       `---'\033[0m \033[32;1m[2.1.9]\033[0m
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
		subprocess.run(['go install -v github.com/projectdiscovery/dnsx/cmd/dnsx@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/dnsx /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/subfinder /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/nuclei /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/tomnomnom/assetfinder@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/assetfinder /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		assets = subprocess.run(['assetfinder -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if assets.returncode == 0:
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
		subprocess.run(['go install github.com/tomnomnom/httprobe@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/httprobe /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/tomnomnom/waybackurls@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/waybackurls /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/tomnomnom/meg@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/meg /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/tomnomnom/gf@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/gf /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/tomnomnom/gron@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/gron /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
	backfin = subprocess.run(['chronos -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if backfin.returncode != 0:
		print("chronos is Not Installed")
		print("Installing chronos")
		subprocess.run(['go install -v github.com/mhmdiaa/chronos@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/chronos /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		backfin1 = subprocess.run(['chronos -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if backfin1.returncode == 0:
			print("\033[32mchronos is installed")
		else:
			print("Failled to Install chronos")
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
		subprocess.run(['go install -v github.com/subfinder/goaltdns@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/goaltdns /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/haccer/subjack@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/subjack /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/ffuf/ffuf@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/ffuf /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
		subprocess.run(['go install -v github.com/hakluke/hakrawler@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/hakrawler /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		hawk1= subprocess.run(['hakrawler -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if hawk1.returncode == 2:
			print("\033[32mhakrawler is installed")
		else:
			print("Failled to Install hakrawler")
	else:
		print("\033[32mhakrawler is installed")


##installing kxss

def kxss_install():
		subprocess.run(['go install -v github.com/Emoe/kxss@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/kxss /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		print("\033[32mKxss is installed")


##installing otxurls

def otxurls_install():
	otxurls= subprocess.run(['otxurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if otxurls.returncode != 0:
		print("otxurls is Not Installed")
		print("Installing otxurls")
		subprocess.run(['go install -v github.com/lc/otxurls@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/otxurls /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		otxurls1= subprocess.run(['otxurls -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if otxurls1.returncode == 0:
			print("\033[32motxurls is installed")
		else:
			print("Failled to Install otxurls")
	else:
		print("\033[32motxurls is installed")


##installing dalfox

def dalfox_install():
	df = subprocess.run(['dalfox -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if df.returncode != 0:
		print("dalfox is Not Installed")
		print("Installing dalfox")
		subprocess.run(['sudo apt install snapd -y',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['sudo snap install dalfox',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		df1 = subprocess.run(['dalfox -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if df1.returncode == 0:
			print("\033[32mdalfox is installed")
		else:
			print("Failled to Install dalfox")
	else:
		print("\033[32mdalfox is installed")


##installing subjs

def subjs_install():
	subjs= subprocess.run(['subjs -version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

	if subjs.returncode != 0:
		print("subjs is Not Installed")
		print("Installing subjs")
		subprocess.run(['go install  -v github.com/lc/subjs@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/subjs /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subjs1= subprocess.run(['subjs -version',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

		if subjs1.returncode == 0:
			print("\033[32msubjs is installed")
		else:
			print("Failled to Install subjs")
	else:
		print("\033[32msubjs is installed")

##installing gau


def gau_install():
	gau = subprocess.run(['gau -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if gau.returncode != 0:
		subprocess.run(['go install -v github.com/lc/gau/v2/cmd/gau@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/gau /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gau1 = subprocess.run(['gau -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gau1.returncode == 0:
			print("\033[32mgau is installed")
		else:
			print("Failled to Install gau")
	else:
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


def godork_install():
	gdork = subprocess.run(['go-dork -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if gdork.returncode != 0:
		print("go-dork is Not Installed")
		print("Installing go-dork")
		subprocess.run(['go install -v dw1.io/go-dork@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/go-dork /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gdork1 = subprocess.run(['go-dork -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gdork1.returncode == 0:
			print("\033[32mgo-dork is installed")
		else:
			print("Failled to Install go-dork")
	else:
		print("\033[32mgau is installed")


def githubsub_install():
	githubsub = subprocess.run(['github-subdomains -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if githubsub.returncode != 0:
		print("github-subdomains is Not Installed")
		print("Installing github-subdomains")
		subprocess.run(['go install -v github.com/gwen001/github-subdomains@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/github-subdomains /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		githubsub1 = subprocess.run(['github-subdomains -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if githubsub1.returncode == 0:
			print("\033[32mgithub-subdomains is installed")
		else:
			print("Failled to Install github-subdomains")
	else:
		print("\033[32mgithub-subdomains is installed")

def gospider_install():
	gospider = subprocess.run(['gospider -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if gospider.returncode != 0:
		print("gospider is Not Installed")
		print("Installing gospider")
		subprocess.run(['go install -v github.com/jaeles-project/gospider@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/gospider /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gospider1 = subprocess.run(['gospider -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gospider1.returncode == 0:
			print("\033[32mgospider is installed")
		else:
			print("Failled to Install gospider")
	else:
		print("\033[32mgospider is installed")

def puredns_install():
	puredns = subprocess.run(['puredns -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if puredns.returncode != 0:
		print("puredns is Not Installed")
		print("Installing puredns")
		subprocess.run(['go install -v github.com/d3mondev/puredns/v2@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/puredns /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		puredns1 = subprocess.run(['puredns -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if puredns1.returncode == 0:
			print("\033[32mpuredns is installed")
		else:
			print("Failled to Install puredns")
	else:
		print("\033[32mpuredns is installed")


def gauplus_install():
	gauplus = subprocess.run(['gauplus -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if gauplus.returncode != 0:
		print("gauplus is Not Installed")
		print("Installing gauplus")
		subprocess.run(['go install -v github.com/bp0lr/gauplus@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/gauplus /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gauplus1 = subprocess.run(['gauplus -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gauplus1.returncode == 0:
			print("\033[32mgauplus is installed")
		else:
			print("Failled to Install gauplus")
	else:
		print("\033[32mgauplus is installed")


def qsreplace_install():
	gauplus = subprocess.run(['qsreplace -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if gauplus.returncode != 0:
		print("qsreplace is Not Installed")
		print("Installing qsreplace")
		subprocess.run(['go install -v github.com/tomnomnom/qsreplace@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/qsreplace /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		gauplus1 = subprocess.run(['qsreplace -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if gauplus1.returncode == 0:
			print("\033[32mqsreplace is installed")
		else:
			print("Failled to Install qsreplace")
	else:
		print("\033[32mqsreplace is installed")

def unfurl_install():
	unfurl = subprocess.run(['unfurl -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if unfurl.returncode != 0:
		print("unfurl is Not Installed")
		print("Installing unfurl")
		subprocess.run(['go install -v github.com/tomnomnom/unfurl@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/unfurl /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		unfurl1 = subprocess.run(['unfurl -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if unfurl1.returncode == 0:
			print("\033[32munfurl is installed")
		else:
			print("Failled to Install unfurl")
	else:
		print("\033[32munfurl is installed")

def naabu_install():
	naabu = subprocess.run(['naabu -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if naabu.returncode != 0:
		print("naabu is Not Installed")
		print("Installing naabu")
		subprocess.run(['sudo apt install -y libpcap-dev',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/naabu /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		naabu1 = subprocess.run(['naabu -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if naabu1.returncode == 0:
			print("\033[32mnaabu is installed")
		else:
			print("Failled to Install naabu")
	else:
		print("\033[32mnaabu is installed")

def httpx_install():
	httpx = subprocess.run(['httpx -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if httpx.returncode != 0:
		print("httpx is Not Installed")
		print("Installing httpx")
		subprocess.run(['go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/httpx /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		httpx1 = subprocess.run(['httpx -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if httpx1.returncode == 0:
			print("\033[32mhttpx is installed")
		else:
			print("Failled to Install httpx")
	else:
		print("\033[32mhttpx is installed")

def dnsrecon_install():
	dnsrecon = subprocess.run(['dnsrecon -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if dnsrecon.returncode != 0:
		print("dnsrecon is Not Installed")
		print("Installing dnsrecon")
		subprocess.run(['git clone https://github.com/darkoperator/dnsrecon.git',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cd dnsrecon; pip3 install -r requirements.txt; sudo python3 dnsrecon/setup.py install',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		dnsrecon1 = subprocess.run(['dnsrecon -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if dnsrecon1.returncode == 0:
			print("\033[32mdnsrecon is installed")
		else:
			print("Failled to Install dnsrecon")
	else:
		print("\033[32mdnsrecon is installed")

def sublist3r_install():
	sublist3r = subprocess.run(['sublist3r -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if sublist3r.returncode != 0:
		print("sublist3r is Not Installed")
		print("Installing sublist3r")
		subprocess.run(['git clone https://github.com/aboul3la/Sublist3r.git',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cd Sublist3r; pip3 install -r requirements.txt; sudo python3 setup.py install',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		sublist3r1 = subprocess.run(['sublist3r -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if sublist3r1.returncode == 0:
			print("\033[32msublist3r is installed")
		else:
			print("Failled to Install sublist3r")
	else:
		print("\033[32msublist3r is installed")

def massdns_install():
	massdns = subprocess.run(['massdns -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if massdns.returncode != 0:
		print("massdns is Not Installed")
		print("Installing massdns")
		subprocess.run(['git clone https://github.com/blechschmidt/massdns.git',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cd massdns; make; cp bin/massdns /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		massdns1 = subprocess.run(['massdns -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if massdns1.returncode == 0:
			print("\033[32mmassdns is installed")
		else:
			print("Failled to Install massdns")
	else:
		print("\033[32mmassdns is installed")

def findomain_install():
	findomain = subprocess.run(['findomain -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if findomain.returncode != 0:
		print("findomain is Not Installed")
		print("Installing findomain")
		subprocess.run(['sudo wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux -O /usr/local/bin/findomain',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['sudo chmod +x /usr/local/bin/findomain',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		massdns1 = subprocess.run(['findomain -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if massdns1.returncode == 0:
			print("\033[32mfindomain is installed")
		else:
			print("Failled to Install findomain")
	else:
		print("\033[32mfindomain is installed")


def gowitness_install():
	gowitness = subprocess.run(['gowitness -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if gowitness.returncode != 0:
		print("gowitness is Not Installed")
		print("Installing gowitness")
		subprocess.run(['go install -v github.com/sensepost/gowitness@latest',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cp ~/go/bin/gowitness /usr/local/bin',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		massdns1 = subprocess.run(['gowitness -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if massdns1.returncode == 0:
			print("\033[32mgowitnessis installed")
		else:
			print("Failled to Install gowitness")
	else:
		print("\033[32mgowitness is installed")

def dnsgen_install():
	sublist3r = subprocess.run(['dnsgen --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if sublist3r.returncode != 0:
		print("dnsgen is Not Installed")
		print("Installing dnsgen")
		subprocess.run(['https://github.com/ProjectAnte/dnsgen.git',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		subprocess.run(['cd dnsgen; pip3 install -r requirements.txt; sudo python3 setup.py install',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		sublist3r1 = subprocess.run(['dnsgen --help',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if sublist3r1.returncode == 0:
			print("\033[32mdnsgen is installed")
		else:
			print("Failled to Install dnsgen")
	else:
		print("\033[32mdnsgen is installed")

def amass_install():
	amass = subprocess.run(['amass -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
	if amass.returncode != 0:
		print("amass is Not Installed")
		print("Installing amass")
		subprocess.run(['sudo snap install amass',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		amass1 = subprocess.run(['amass -h',], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
		if amass1.returncode == 0:
			print("\033[32mamass is installed")
		else:
			print("Failled to Install amass")
	else:
		print("\033[32mamass is installed")


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
	godork_install()
	githubsub_install()
	gospider_install()
	puredns_install()
	gauplus_install()
	qsreplace_install()
	unfurl_install()
	naabu_install()
	httpx_install()
	dnsrecon_install()
	sublist3r_install()
	massdns_install()
	findomain_install()
	gowitness_install()
	dnsgen_install()
	amass_install()



