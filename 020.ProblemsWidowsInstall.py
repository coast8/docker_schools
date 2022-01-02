
========================================================

problems encountered in 2021, install docker tool-box

========================================================

1. delete AppData/docker
2. delete .docker



-- find AppData
https://cibersistemas.pt/tecnologia/appdata-onde-encontrar-a-pasta-appdata-no-windows-10/#:~:text=Procure%20por%20%E2%80%9CExecutar%E2%80%9D%20na%20janela,est%C3%A1%20dentro%20da%20pasta%20AppData.

-- Desabilitar o Hyper-V no PowerShell
https://docs.microsoft.com/pt-br/troubleshoot/windows-client/application-management/virtualization-apps-not-work-with-hyper-v

-- desable hypervisor
https://stackoverflow.com/questions/50053255/virtualbox-raw-mode-is-unavailable-courtesy-of-hyper-v-windows-10



-- VirtualBox upgrade (5.22 to 5.24 ) and reboot pc.
https://github.com/docker/machine/issues/4066

-- Vitual Box Old_Builds V5
https://www.virtualbox.org/wiki/Download_Old_Builds_5_2








========================================================

problems encountered in 2020

========================================================

# Diseble Hyper-V
https://stackoverflow.com/questions/36885985/cannot-start-docker-after-installation-on-windows
Open Control Panel -> System and Security -> Programs (left panel) -> Turn Windows features on or off -> Check the Hyper-V box




https://forums.docker.com/t/docker-for-windows-image-operating-system-linux-cannot-be-used-on-this-platform/28936

	image operating system “linux” cannot be used on this platform



https://github.com/docker/for-win/issues/1825
	cd "C:\Program Files\Docker\Docker"
	./DockerCli.exe -SwitchDaemon
