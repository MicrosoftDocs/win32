---
Description: Microsoft Corporation
ms.assetid: 4cbe0dbb-de18-4732-b4d7-b892b816b459
title: Driver Chain Manager in Windows XP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Driver Chain Manager in Windows XP

Microsoft Corporation

Revised June 2008

**Summary:** Learn how Driver Chain Manager (DCM) helps reduce the errors that users of assistive technology products can experience when they have multiple screen readers, screen magnifiers or remote access software installed on their computers. (7 printed pages)

Download the [DCMSetup.exe](http://go.microsoft.com/fwlink/p/?linkid=208736) code sample.

-   [The Problem](#the-problem)
-   [What is the Driver Chain Manager?](#what-is-the-driver-chain-manager)
    -   [What Capabilities does DCM Provide?](#what-capabilities-does-dcm-provide)
    -   [Issues Yet to Address](#issues-yet-to-address)
-   [Becoming DCM-Enabled](#becoming-dcm-enabled)
    -   [Additional Information](#additional-information)
    -   [Future Plans](#future-plans)
-   [Product Updates](#product-updates)
-   [Driver Chain Manager FAQ](#driver-chain-manager-faq)
    -   [What is Driver Chain Manager?](#what-is-driver-chain-manager)
    -   [Who Created DCM?](#who-created-dcm)
    -   [Who Owns DCM?](#who-owns-dcm)
    -   [Which Operating Systems Does it Support?](#which-operating-systems-does-it-support)
    -   [Does DCM Support Multiple Monitors?](#does-dcm-support-multiple-monitors)
    -   [Does DCM Support Terminal Service Sessions?](#does-dcm-support-terminal-service-sessions)
    -   [What Problems Does DCM Solve?](#what-problems-does-dcm-solve)
    -   [How Does DCM Work?](#how-does-dcm-work)
    -   [Which Assistive Technology Vendors use DCM?](#which-assistive-technology-vendors-use-dcm)
    -   [How is DCM Installed?](#how-is-dcm-installed)
    -   [Can I Uninstall DCM?](#can-i-uninstall-dcm)
    -   [Does the Order in Which Assistive Technology Aids are Installed Matter?](#does-the-order-in-which-assistive-technology-aids-are-installed-matter)
    -   [How Do I Upgrade?](#how-do-i-upgrade)
    -   [Can I Use DCM with My Existing Assistive Technology Software?](#can-i-use-dcm-with-my-existing-assistive-technology-software)
    -   [What About Remote Control Software?](#what-about-remote-control-software)
    -   [Which Versions of Assistive Technology Aids Support DCM?](#which-versions-of-assistive-technology-aids-support-dcm)
    -   [How Do I Upgrade Assistive Technology Aids?](#how-do-i-upgrade-assistive-technology-aids)
    -   [Can I Run Multiple Assistive Technology Aids at the Same Time?](#can-i-run-multiple-assistive-technology-aids-at-the-same-time)
    -   [What is the Chain Order?](#what-is-the-chain-order)
    -   [Do I Need to Adjust the Chain Order?](#do-i-need-to-adjust-the-chain-order)
    -   [How Do I Adjust the Chain Order?](#how-do-i-adjust-the-chain-order)
    -   [How Do I Know the Right Chain Order?](#how-do-i-know-the-right-chain-order)
    -   [Why Do I Need to Adjust the Chain Order?](#why-do-i-need-to-adjust-the-chain-order)
    -   [How Can I Learn More About DCM?](#how-can-i-learn-more-about-dcm)

## The Problem

With screen reading or screen magnification software, assistive technology vendors (ATVs) essentially locate the display driver, get the information needed for it, then pass the sometimes modified Display Driver Interface (DDI) calls to the original display driver. (Certain remote control software also uses this technique to intercept information being passed to a remote computer.) The DDI interception technique is called *driver chaining*.

The major problem with driver chaining today is that there are no rules governing how drivers work with each other. Consequently, chain drivers are not always aware of each other's existence; a given driver cannot know what other driver precedes or follows it. When there are multiple drivers due to the presence of several screen readers, magnifiers, remote software, or even demo assistive technology software, there may be a long set of drivers chained together. The last driver in the sequence is the actual driver known to and used by the system to write to the display hardware.

Driver chains can become so corrupted that the system can no longer find the "real" display driver and, therefore, defaults to VGA mode or becomes unstable and crashes.

For example, a user installs software A and then software B. Suddenly, software A stops magnifying or reading certain objects on the screen, even when software B is not running. If the user then uninstalls software A, it may or may not uninstall; but, regardless, it can cause software B to no longer function. The chain may become corrupted to an extent that the system can no longer find the real display driver and defaults to VGA mode.

## What is the Driver Chain Manager?

Driver Chain Manager (DCM) is a result of a joint project involving Ai Squared, Dolphin Computer Access, Freedom Scientific, GW Micro and Microsoft.

DCM is a set of helper libraries that implement rules about how multiple DDI interceptors cooperate with each other on Microsoft Windows 2000, Windows XP and any other Windows operating system that supports DCM.

> [!Note]  
> Driver chaining is generally not a recommended approach because a driver is never meant to be replaced or modified, and DDI calls are not meant to be intercepted.

 

Having multiple chained drivers compounds an already complex situation. At present, however, the screen reader and magnifier vendors do not have an alternative way to get full information about what is drawn on the screen. DCM was created to reduce the errors caused by driver chaining. The DCM helper libraries essentially manage the reading and writing of information in the registry about how chain drivers are chained onto each other and eventually chained to the real display driver.

There are currently three long-term assistive technology interoperability goals for the Windows environment to which Microsoft is committed:

-   Provide sufficient information about objects on the screen.
-   Ensure that other assistive technologies installed on a system will not interfere with the proper functioning of assistive technology software already running.
-   Ensure that multiple assistive technology applications can run together.

Driver Chain Manager 1.0 is a step toward meeting these goals.

### What Capabilities does DCM Provide?

DCM provides for the following:

-   When multiple DCM chain drivers are installed, as long as only one is active, the others should not impact the active driver regardless of its position in the chain.
-   A user can install and uninstall DCM chain drivers in any order without affecting the other drivers.
-   There are workarounds for common remote control software that also rely on chaining.
-   All DCM chain drivers use the same escape code to handle communication between their user and driver modules.
-   If the display adapter is changed, it is detected so proper adjustment of the chain can be carried out.
-   For vendors who support DCM, their existing drivers installed in a user's system do not interfere with installation of new DCM drivers.

### Issues Yet to Address

There are several issues that are beyond the scope of DCM. They are:

-   DCM does not guarantee that multiple DCM chain drivers running actively together will function properly. At this point, it is up to the particular vendors to make sure that their software can actively run well together.
-   For vendors who support DCM, their previous drivers may remain after some DCM chain drivers have been installed. However, DCM would not know about these earlier drivers.
-   There are other unknown, non-DCM drivers that can be installed, but DCM would not know about them.
-   DCM does not handle the scenario of a user with multiple monitors.

## Becoming DCM-Enabled

Producing a DCM-enabled set of drivers involves the following:

1.  Make sure that your driver is indeed relaying all DDI calls when inactive.
2.  Do not statically link the DCMUser.dll and DCMKrnl.dll files.
3.  Submit the INI file entries and DLLs for previous driver handling.
4.  Run DCMSetup.exe in the Installer to install or copy the helper DLLs into the Windows system32 folder.
5.  Make certain the Installer calls PutDriverInChain to add your driver to the chain.
6.  If you want to uninstall a chain driver, Uninstaller should call the RemoveDriverFromChain and RemoveDriverInfo files to clean up the driver chain.
7.  The run-time chain driver should call GetNextDriver in response to DrvEnableDriver.
8.  The run-time user-level module should call CheckChainIntegrity during every startup. This will help maintain the integrity of the chaining.
9.  Make certain that GetCurrentDisplayDriver and GetChainDriverInfo can be called at any time.
10. Make certain the run-time chain driver knows how to respond to DCM\_STANDARD\_ESCAPE\_CODE.
11. Do adequate testing with the driver, including the Hardware Compatibility Testing (HCT) suite.

### Additional Information

Vendors interested in understanding and redistributing DCM may download documentation and distributable modules from the link at the beginning of this article.

> [!Note]  
> DCM is not an end-user component. DCM is always tightly coupled with vendor products and is made available to users through these products.

 

If you are a vendor who would like to implement DCM in your products, please contact Microsoft at enable@microsoft.com.

If you are a user of assistive technology products who is seeking support regarding DCM, please contact your assistive technology vendor.

### Future Plans

When the DCM specification and code matures, Microsoft may turn over management and maintenance of the DCM source code to an industry entity.

## Product Updates

DCM Update 1.020

This update addresses some crashes that occurred when users accessed the Settings tab on the Control Panel on a computer that contained certain video cards from Intel and ATI that supported dual-displays.

This is an ongoing issue. Microsoft is working toward a long-term solution with its DCM partner organizations Ai Squared, Dolphin Computer Access, GW Micro, and Freedom Scientific.

> [!Note]  
> We are working to prevent crashes when video cards that support multiple displays are used in a single display configuration with DCM. DCM is not intended to enable DDI hooking on two displays simultaneously.

 

DCM Update 1.020 will be made available via this page in the near future. Vendors who are currently shipping DCM have already made it available to their customers as part of their AT products.

## Driver Chain Manager FAQ

Following is a list of commonly asked questions about the Microsoft Driver Chain Manager (DCM).

### What is Driver Chain Manager?

DCM is a new technology from Microsoft whose purpose is to allow multiple assistive technology aids that use display driver interception (DDI) to be installed in the same computer. DCM is aimed primarily at screen readers and screen magnifiers.

### Who Created DCM?

DCM is the result of a joint effort between Microsoft and partner organizations, Ai Squared, Dolphin Computer Access, GW Micro, and Freedom Scientific.

### Who Owns DCM?

It is owned and maintained by Microsoft. A future version might be owned by an industry organization.

### Which Operating Systems Does it Support?

DCM 1.0 supports Microsoft Windows NT version 4, Windows 2000, and Windows XP.

### Does DCM Support Multiple Monitors?

No, it does not.

### Does DCM Support Terminal Service Sessions?

No, it does not.

### What Problems Does DCM Solve?

Having multiple assistive technology aids installed in a computer can lead to crashes, boot failures, and malfunctioning software. These problems often prevented installation of more than one assistive technology aid in the same computer.

### How Does DCM Work?

DCM is a set of library routines used by each assistive technology aid to install, remove, and maintain their graphics driver interceptors. Because a common library is used, installation and removal of interceptors is done in a compatible manner between different assistive technology aids.

### Which Assistive Technology Vendors use DCM?

To date, Ai Squared, Dolphin Computer Access, GW Micro, and Freedom Scientific are planning to release DCM-enabled versions of their software. Assistive technology aids by these vendors include:

-   Hal, Lunar, LunarPlus, and Supernova by Dolphin Computer Access
-   JAWS and MAGic by Freedom Scientific
-   Window-Eyes by GW Micro
-   ZoomText by Ai Squared

### How is DCM Installed?

The latest version of the DCM Library is installed automatically (in the same way as Microsoft Active Accessibility is) when you install or upgrade an assistive technology aid that is DCM-enabled.

### Can I Uninstall DCM?

No. The DCM Library is an integral part of the operating system and cannot be uninstalled. You can, however uninstall all assistive technology aids. If no DCM-enabled assistive technology aids exist, the DCM Library will not be used.

### Does the Order in Which Assistive Technology Aids are Installed Matter?

No. DCM-enabled assistive technology aids can be installed in any order.

### How Do I Upgrade?

If you have already installed non-DCM-enabled assistive technology aids, then you should upgrade them to a DCM-enabled version before attempting to install any other aids.

If you install a DCM-enabled aid at the same time as a non-DCM–enabled aid, one or more of your assistive technology aids may not work correctly.

### Can I Use DCM with My Existing Assistive Technology Software?

No. You need to upgrade to a DCM-enabled version of your assistive technology aid from your vendor.

### What About Remote Control Software?

The DCM Library contains code to handle certain other software that uses display driver interceptors, such as PCAnyware, LapLink and ControlIT. In many cases, these other applications will be compatible with your DCM assistive technology software.

### Which Versions of Assistive Technology Aids Support DCM?

The following assistive technology aids support DCM:

-   Hal 5.20 and higher
-   JAWS 4.51 and higher
-   MAGic 8.1 and higher
-   Lunar 5.20 and higher
-   LunarPlus 5.20 and higher
-   Supernova 5.20 and higher
-   Window-Eyes 4.21 and higher
-   ZoomText 7.11 with driver utility program (request from Ai Squared)
-   ZoomText 8.0 and higher (DCM built-in)

### How Do I Upgrade Assistive Technology Aids?

Contact the vendor of your assistive technology aid for upgrade information. Ai Squared, Dolphin Computer Access, GW Micro, and Freedom Scientific are planning to release DCM-enabled versions of their products.

### Can I Run Multiple Assistive Technology Aids at the Same Time?

DCM was designed to allow you to have multiple assistive technology aids installed in the same computer, but it does not ensure that you can run them at the same time. However, tests have shown that in many cases you can run several assistive technology aids simultaneously without major problems. You may, however, need to first determine the correct chain order.

### What is the Chain Order?

The chain order is the order in which the different drivers appear in the display chain. Some drivers, such as screen readers, pass through information to the next driver in the chain, so subsequent drivers work correctly. Other drivers, such as those for screen magnifiers, modify the information when they are active (they magnify it), causing the drivers that follow them to work incorrectly.

### Do I Need to Adjust the Chain Order?

If, at a given instance, you are running only one assistive technology aid, or aids from a single software vendor, then you do not need to adjust the chain order. If you are running assistive technology aids from different vendors, then most of the time the chain order will be correct. If your software works as expected then your chain order is probably correct.

### How Do I Adjust the Chain Order?

A utility program called DCMUTIL.EXE is provided with your assistive technology aid for this purpose. It is recommended that you contact your vendor's technical support department for assistance using the DCMUTIL program.

### How Do I Know the Right Chain Order?

There are no hard and fast rules about this, but you basically need to ensure that the driver that comes with your screen reader is before the one for your magnifier.

### Why Do I Need to Adjust the Chain Order?

Some drivers perform both screen reading and screen magnification. An example of this is the driver used by JAWS and MAGic (by Freedom Scientific). If you have two such drivers from two different software vendors, however, there is no correct order that will work in all circumstances. It depends on which screen reader and magnifier you plan to run.

### How Can I Learn More About DCM?

Check the following websites for additional information about DCM 1.0:

[Assistive Technology Products](http://go.microsoft.com/fwlink/p/?linkid=165634) provides general information about Microsoft assistive technologies.

The MSDN Library provides links to various developer sites. Choose the **User Interface Design and Development** topic and click **Accessibility** for a variety of technical articles on and information about assistive technologies, including DCM.

If you are a vendor who would like to implement DCM in your products, please send email to enable@microsoft.com.

If you are a user of assistive technology products who is seeking support regarding DCM, please contact your assistive technology vendor.

 

 



