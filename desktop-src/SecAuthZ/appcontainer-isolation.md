---
description: Isolation is the primary goal of an AppContainer execution environment.
ms.assetid: 13C579F9-7F9F-4602-9B03-08CD820C3BBA
title: AppContainer Isolation
ms.topic: article
ms.date: 05/31/2018
---

# AppContainer Isolation

Isolation is the primary goal of an AppContainer execution environment. By isolating an application from unneeded resources and other applications, opportunities for malicious manipulation are minimized. Granting access based upon least-privilege prevents applications and users from accessing resources beyond their rights. Controlling access to resources protects the process, the device, and the network.

Most vulnerabilities in Windows start with the application. Some common examples include an application breaking out of its browser or sending a bad document to Internet Explorer as well as exploitation of plugins, such as flash. The more these applications can be isolated in an AppContainer, the safer the device and resources are. Even if vulnerability in an app is exploited, the app cannot access resources beyond what is granted to the AppContainer. Malicious apps cannot take over the rest of the machine.

## Credential Isolation

Managing identity and credentials, the AppContainer prevents the use of user credentials to gain access to resources or login to other environments. The AppContainer environment creates an identifier that uses the combined identities of the user and the application, so credentials are unique to each user/application pairing and the application cannot impersonate the user.

## Device Isolation

Isolating the application from device resources, such as passive sensors (camera, microphone, GPS), and money pumps (3G/4G, dial phone) the AppContainer environment prevents the application from maliciously exploiting the device. These resources are blocked by default and can be granted access as necessary. In some cases these resources are further protected by 'brokers'. Some resources, such as keyboard and mouse, are always available to the AppContainer and resident application.

## File Isolation

Controlling file and registry access, the AppContainer environment prevents the application from modifying files that it should not. Read-write access can be granted to specific persistent files and registry keys. Read-only access is less restricted. An application always has access to the memory resident files created specifically for that AppContainer.

## Network Isolation

Isolating the application from network resources beyond those specifically allocated, AppContainer prevents the application from 'escaping' its environment and maliciously exploiting network resources. Granular access can be granted for Internet access, Intranet access, and acting as a server.

## Process Isolation

Sandboxing the application kernel objects, the AppContainer environment prevents the application from influencing, or being influenced by, other application processes. This prevents a properly contained application from corrupting other processes in the event of an exception.

## Window Isolation

Isolating the application from other windows, the AppContainer environment prevents the application from affecting other application interfaces.

 

 



