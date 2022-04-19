from typing import Iterable
import distro
import os
import typer
import abc
#note: I should work on mac soon, because I will need this for mac in may
app = typer.Typer()
def TODO(s):
    raise Exception("TODO: " +s)

def is_installed(command):
    return os.system("command -v "+command) == 0

def get_shell():
    return os.system("echo #SHELL")


class PackageManager(metaclass=abc.ABCMeta):
    
    @abc.abstractclassmethod
    def install(self, deps: Iterable[str]):
        return True


class AptGet(PackageManager):

    def __init__():
        if not AptGet.aptInstalled():
            raise Exception("apt is not installed")

    @staticmethod
    def aptInstalled():
        return is_installed("apt") or is_installed("apt-get")
        
    def install(self, deps: Iterable[str]):
       os.system("sudo apt-get install "+" ".join(deps))


class NvimSetup:

    def __init__(self,manager: PackageManager): 
        assert get_shell() == "/bin/zsh"
        self.manager = manager

    def install_deps_arch(self):
        TODO("add arch linux support") # it's just not worth it, since I'm not updating my pc anytime soon
 
    def setup(self):
        self.manager.install(["neovim", "zsh"])
        setup_config = """
        cp ./init.vim ~/.config/nvim/init.vim
        cp .vimrc ~/.vimrc
        cat ./.zshrc > ~/.zshrc
        source ~/.zshrc
        vim -c PlugInstall
        """
        os.system(setup_config)


        
@app.command()
def setup_zsh():
    TODO("add setup zsh")


@app.command()
def setup_nvim():
    NvimSetup(AptGet()).setup();



if __name__ == "__main__":
    app();

