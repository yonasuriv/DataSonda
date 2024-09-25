
<p align="center">
  <img src="https://github.com/user-attachments/assets/4b989b4a-f449-41f4-b290-d5a573754da2"/>
</p>

----

## Description

Sonda SysNet is designed to be a comprehensive utility that combines the features of nearly all system information tools available on Linux. Whether you need details on system uptime, active processes, hardware specifications, network configurations, or package versions, Sonda SysNet brings all this information into a single, easy-to-use interface.

With real-time terminal notifications, you can keep track of important system events like package updates, disk space usage, memory allocation, CPU load, and much more. Sonda SysNet is especially useful for system administrators, developers, and power users who need a reliable and fast way to get accurate system details.

----

## Features

**Comprehensive System Information**: 
- Hardware specifications, CPU, RAM, storage devices, and more.
- Detailed system uptime and load averages.
- Live monitoring of system resources (CPU usage, memory, disk space).

**Network Details**: 
- Displays network interfaces, IP addresses, routing information, and active connections.
- Current IP addresses (local and public), MAC addresses, and more.
- Active network connections, listening ports, and firewall status.
- Network interface details and traffic statistics.

**Package Management**: 

- Live tracking of installed packages and available updates.
- Notifications for package updates, both system-wide and user-specific.
- List of installed and pending packages with details on version numbers.

**Live Notifications**: 
- Live updates displayed directly in the terminal.
- Notifications for package installations, system events, or changes in network status.

**System Health Monitoring**: 
- Tracks CPU usage, memory consumption, disk space, and system uptime.

**Process Management**: 
- Displays all running processes, allowing you to monitor resource usage in real-time.

**Real-Time Resource Monitoring**: 
- Monitors system performance, including CPU, memory, and network usage.

**Easy-to-Use Interface**: 
- Clear, terminal-friendly interface that presents detailed information in a concise format.
  
**Comprehensive Output**:

- Outputs detailed and readable information for both system administrators and users.
- Optionally logs data for future analysis.

**OS Integration**:

- Seamlessly integrates with system services like systemd to provide a full picture of the system’s status.

**Modular Design**: 
- Easy to extend and customize for specific use cases.
- Features can be selectively enabled or disabled based on user needs.

## Compatibility

Sonda SysNet is tested and fully functional on the following GNU/Linux distributions:

- **Kali Linux 24.3 Rolling Release**


> This in no way means that it doesn't work on other distributions, even less so on those based on Debian.
>
> It's just that due to lack of time I have not been able to proceed further.
>
> **Additional distributions will be supported in the future.**

## Installation
To install Sonda SysNet, simply clone the repository and run the setup script:

```bash
git clone https://github.com/yonasuriv/sondasysnet && cd sondasysnet && ./MAKEFILE -i
```

All requirements and dependencies are handled automatically. To uninstall it run `./MAKEFILE -u`

Once installed, you can run Sonda SysNet from the terminal:

```bash
sonda
```

This will provide a comprehensive, real-time overview of your system and network information, depending on the argument passed.

## Usage

----

<p align="center"> 
  <img src="https://github.com/user-attachments/assets/4bc2318c-bd99-4c10-968b-4a1359ed3e31"/>
</p>

----

### Example Command Output

> **The following output consists of image copies from a TXT file to prevent revealing unnecessary information due to time constraints.**
> The tool is visually appealing and will continue to improve over time, adapting to various needs and scenarios.

#### -s argument

<p align="center">
  <img src="https://github.com/user-attachments/assets/1e71d4b6-a201-4db5-811b-4b3db4fd5c71"/>
</p>

#### -n argument:

<p align="center">
  <img src="https://github.com/user-attachments/assets/4ae89af0-f96c-42fc-9058-f0a6bfa42163"/>
</p>

## Support
To contribute or get support, simply fork the repository and submit your issues or pull requests. 

All forms of contributions are welcome, from bug fixes to new features and OS compatibility testing.

## License
Sonda SysNet is open-source software licensed under the MIT License. See the LICENSE file for more details.
