# Ansible playbooks 📚
Ansible playbooks assume you have private key setup already. Everything will be done via ssh for Unix based system.

```bash
# Arch
pacman -S python, python-pip, unzip

# Debian 
apt install python3-pip, unzip

curl -LO https://github.com/4542elgh/Dotfiles_Ansible/archive/refs/heads/main.zip $HOME/main.zip
unzip $HOME/main.zip

cd $HOME/Dotfiles_Ansible-main

ansible-playbook -i inventory/inventory.yml playbook.yaml
```
