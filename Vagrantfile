# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/precise64"

  config.ssh.insert_key = false

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.provision "init", type: "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y vim
    apt-get install -y python
    apt-get install -y pylint
    apt-get install -y git
    apt-get install -y make
    apt-get install -y curl
  SHELL

  config.vm.provision "init-vim", type: "shell", privileged: false, inline: <<-SHELL
    git clone https://github.com/JohnVanNote/dotfiles.git ~/dotfiles/
    cd ~/dotfiles
    make
  SHELL

end
