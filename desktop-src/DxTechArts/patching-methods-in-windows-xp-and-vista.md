---
title: Patching Game Software in Windows XP, Windows Vista, and Windows 7
description: This article examines some methods of patching that will work well in Windows Vista and Windows 7, as well as Windows XP.
ms.assetid: 27be805a-bffd-a9f8-2207-2a9a4822ba48
ms.topic: article
ms.date: 05/31/2018
---

# Patching Game Software in Windows XP, Windows Vista, and Windows 7

Windows Vista and Windows 7 have a number of features to make the operating system more secure. Added security means that applying patches to software is not as simple as it was in the past. This article examines some methods of patching that will work well in Windows Vista and Windows 7, as well as Windows XP.

There are two main categories of games that require patches:

-   Games that require only occasional patches, such as most offline games.
-   Games that require frequent patches, such as most online games.

This article also offers a brief introduction to the User Account Control (UAC) to serve as background about the rights that developers can expect users to have in Windows Vista and Windows 7.

-   [User Account Control](#user-account-control)
-   [Games that Require Only Occasional Patches](#games-that-require-only-occasional-patches)
    -   [Method 1: Use Windows Installer for Occasional Patches](#method-1-use-windows-installer-for-occasional-patches)
    -   [Method 2: Require Administrator Rights to Apply Patches](#method-2-require-administrator-rights-to-apply-patches)
-   [Games that Require Frequent Patches](#games-that-require-frequent-patches)
    -   [Method 3: Install Per-User](#method-3-install-per-user)
    -   [Method 4: Install to a Common Per-Computer Location](#method-4-install-to-a-common-per-computer-location)
    -   [Other Possibilities](#other-possibilities)
-   [Summary](#summary)

## User Account Control

Windows Vista and Windows 7 have two primary types of user accounts: Standard User and Administrator. A Standard User account has several access restrictions; for example, it cannot write data to the file system in %SystemDrive%\\Program Files or to the registry in the HKEY\_LOCAL\_MACHINE. This has implications for applying patches to a game if it is installed in a read-only location. Unlike in Windows XP, the Standard User account is much more common in Windows Vista and Windows 7. Standard User accounts are also required for important features of the operating system, like parental controls. Parental controls require that the child account be Standard User, and elevating such an account to Administrator for even one game prevents parental controls from working with all other games. So, it important for games to be designed for Standard User.

Windows Vista and Windows 7 have a newer model for user rights, to help prevent users from running programs that attempt to perform operations that the user doesn't intend or authorize. To that end, User Account Control (formerly called Least-privileged User Account or LUA) enables users to operate the computer with low-level rights most of the time, while being able to easily run applications that require higher-level rights, when necessary. This means that Standard User accounts and Administrator accounts both run applications with Standard User rights, but only Administrator accounts have the ability to grant elevated rights to applications. The operating system asks users with Administrator accounts for explicit consent before running an application with elevated rights, and if a program that requires Administrator rights is run on a Standard User account, the system prompts for Administrator approval.

## Games that Require Only Occasional Patches

Some games only require a few patches throughout their lifecycle. Two methods that you can employ for this frequency of patching are to distribute patches as Windows Installer packages, which does not generally require Administrator rights, or to use some other type of distribution that directly modifies game files.

> [!Note]  
> Regardless of whether a game requires frequent patching, applications typically require Administrator rights to be installed or removed.

 

### Method 1: Use Windows Installer for Occasional Patches

In this method, a Windows Installer is used to install a package (.msi file) and a Windows Installer patch (.msp file) is distributed to install patches. The package must have an MsiPatchCertificate table, and the patch must be digitally signed by a certificate in the table. More information about digital signing can be found at [Authenticode Signing for Game Developers](/windows/desktop/DxTechArts/authenticode-signing-for-game-developers).

More details and requirements to use this patching method can be found in the Windows Installer documentation:

-   [Patching and Upgrades](/windows/desktop/Msi/patching-and-upgrades)
-   [User Account Control (UAC) Patching](/windows/desktop/Msi/user-account-control--uac--patching)

The disadvantage to this method is that if the game was not installed from removable media on Windows XP, then patching requires Administrator rights. However, this not likely to be too restrictive, because most users administrators on Windows XP, and the restriction to software installed from removable media is not present on Windows Vista.

The main advantage of this method is that patches can be applied by a Standard User account without requiring a prompt and authentication for elevated rights. This provides a better user experience, because to play a game, a user with a Standard User account doesn't need to ask someone with an Administrator account to install the patch or to provide the Standard User account with permanent Administrator rights.

It is possible that this method might work for games that require frequent patches, but the overhead of using Windows Installer packages, in terms of build integration and supporting large numbers of files, might make this method less desirable than others.

### Method 2: Require Administrator Rights to Apply Patches

In this method, the executable file that applies the patch requires Administrator rights to run. With Administrator rights, the patching executable can directly modify the game files located in %SystemDrive%\\Program Files.

The advantage of this method is its simplicity. However, this method is unsuitable if the game needs frequent patches, because if a user with a Standard User account wants to play a game that requires frequent patches, like a massively multi-player online game, then that user has two choices:

-   Get an Administrator to log on and patch the game, which might be inconvenient for both parties.
-   Have his or her account permanently elevated with Administrator rights.

> [!Note]  
> The latter solution not only weakens the security of the system as a whole, but it prevents important features, like parental controls, from working.

 

When implementing this method, the executable file that applies the patch must be different from the game executable. The manifest of the patching executable should specify requireAdministrator for requestedExecutionLevel to denote it as an application that requires Administrator rights. More information about how to do this can be found at [Developer Best Practices and Guidelines for Applications in a Least Privileged Environment](/previous-versions/dotnet/articles/aa480150(v=msdn.10)), in "Application Manifest Schema."

When this method is used, even with the settings in the manifest, the executable file might still be launched without Administrator rights in two cases:

-   If the operating system is Windows XP, and the user's account is a Restricted User.
-   If the operating system is Windows Vista or Windows 7, the user's account is a Standard User, and UAC is disabled.

Both of these are rare consumer scenarios. However, the patcher should have the manifest require Administrator rights, and it should call [**IsUserAnAdmin**](/windows/desktop/api/shlobj_core/nf-shlobj_core-isuseranadmin); if this function returns FALSE, the error message "Administrator rights are required" is displayed.

Overall, method 1 is preferable for games that need just a few patches over their lifetimes.

## Games that Require Frequent Patches

Many Internet-based games are being improved continuously, and they usually require regular patches. For these games, patches could be applied per-user or per-computer, as discussed in the follow topics. Other possible solutions include altering the ACL that protects %SystemDrive%\\Program Files or creating a custom service.

### Method 3: Install Per-User

One recommended and easy approach is to install the entire game to a per-user subfolder of the local application data folder, which you can find by calling [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) with CSIDL\_LOCAL\_APPDATA. An example path is C:\\Documents and Settings\\user name\\Local Settings\\Application Data\\ExampleGame. Such a location allows an application running with Standard User rights to directly modify game files.

However, there is a disadvantage to this approach when a computer has multiple users: each user has a copy of the game installed, and patches must be downloaded and applied by each user. This wastes not only users' time and disk space, but it also increases use of network bandwidth to the server that provides patches. Also, because any application with standard user rights can modify the game, game executables are less protected; it is up to the game manufacturer to decide if this is acceptable or not.

### Method 4: Install to a Common Per-Computer Location

Another method is to install the non-executable game data to a subdirectory of the path specified by [**SHGetFolderPath**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetfolderpatha) CSIDL\_COMMON\_APPDATA; an example path is C:\\Documents and Settings\\All Users\\Application Data\\ExampleGame. This is a shared location for all users, and it can be modified by applications that run with Standard User rights. This method minimizes the need to reapply large patches when the game is played from more than one account. Executable files for the game should be kept in %SystemDrive%\\Programs Files to minimize the risk to other accounts on the system. The executable files should verify the integrity of the new content in the shared directory, since that location can be modified by a program or person with Standard User rights; consider using [**MapFileAndCheckSum**](/windows/desktop/api/imagehlp/nf-imagehlp-mapfileandchecksuma) to compute a checksum of the files.

This method has the advantage of working equally well on both Windows XP and Windows Vista, and it doesn't require Administrator rights.

### Other Possibilities

Outside of the methods already discussed, another possibility is to alter the ACL of %SystemDrive%\\Program Files\\Game Folder\\ when installing the game so that a patching tool can write directly to the game's files even when run with Standard User rights. While this is not difficult, it does bypass the security protection that the system offers to the game's files and provides an opportunity for malicious programs to alter the contents of the directory. This is not advisable, and it is strongly recommended that an alternative be used instead.

One final possibility is to write a custom service. In general, writing a custom service to patch games is not a good idea, because doing so is complicated and error-prone. It is recommended that patching be done by use of other methods discussed in this article. However, a custom service might be necessary when combined with anti-cheat or anti-piracy solutions. Such a service should support a large number of games and be designed so that it can only download the patch files and write only to the installation directory for the target game. It is important that the service be small, have a minimal surface area that is vulnerable to attack, and use as few system resources as possible when the game is not running.

## Summary

Ultimately, it is up to you to decide which method to implement. You need to weigh the factors are that are important to you. Security, frequency of patching, ease of use by customer, workload required to implement, complexity of solution, and platform feature compliance are the factors that each developer must consider before deciding on a particular method.

You can find more information about user account protection in [Windows Vista Application Development Requirements for User Account Control (UAC)](/previous-versions/aa905330(v=msdn.10)).

 

 