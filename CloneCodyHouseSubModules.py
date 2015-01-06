from git import * 
import time
import os 
import requests 
import simplejson as json

now = time.asctime(time.gmtime())

CodyPath = './CodyBlueprints/'

if (os.path.exists(CodyPath)):  
  new_repo = Repo(CodyPath) 
else: 
  new_repo = Repo.init(CodyPath) 

ff = open('./CodyBlueprints/Updated.txt','w')
ff.write( "Repo Updated: %s " % now ) 
ff.close() 

git = new_repo.git
git.add("*")

r = requests.get('https://api.github.com/users/CodyHouse/repos')
JD = json.JSONDecoder() 
gitrepos = JD.decode(r.text) 

reposlist = [] 

for item in gitrepos: 
   reposlist.append(item['clone_url']) 

for item in reposlist: 
    gitrepo = item 
    repo_dir = "%s" % (gitrepo.split('/')[-1].split('.')[:-1])[0]
    repo_dir = CodyPath + repo_dir 
    print repo_dir 
    try: 
      Repo.clone_from(gitrepo, repo_dir)
    except: 
      print "SKIPPING       ------ %s into %s " % (gitrepo, repo_dir) 
 

#sms = repo.submodules
#print sms 
