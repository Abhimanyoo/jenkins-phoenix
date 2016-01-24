import jenkins

# cf: https://updates.jenkins-ci.org/download/plugins/

j = jenkins.Jenkins('http://jenkins:8080')
#print 'Plugins:'
#print j.get_plugins()
print 'Installing plugins starting'
info = j.install_plugin("docker-plugin")
info = j.install_plugin("git")
info = j.install_plugin("github")
info = j.install_plugin("urltrigger")
print 'Installing plugins done'



#install_plugin(self, name, include_dependencies=True)
#    Install a plugin and its dependencies from the Jenkins public
#    repository at http://repo.jenkins-ci.org/repo/org/jenkins-ci/plugins
#    
#    :param name: The plugin short name, ``string``
#    :param include_dependencies: Install the plugin's dependencies, ``bool``
#    :returns: Whether a Jenkins restart is required, ``bool``
#    
#    Example::
#        >>> info = server.install_plugin("jabber")
#        >>> print(info)
#        True

