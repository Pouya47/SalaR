import subprocess   
cmd="ruby fakestack.rb"                                                                          
p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)                              
output, errors = p.communicate()
print 'OUTPUT='+output
print '_'*50
print 'Errors='+str(errors)
