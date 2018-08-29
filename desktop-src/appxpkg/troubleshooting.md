---
title: Troubleshooting packaging, deployment, and query of Windows Store apps
description: Use these suggestions to troubleshoot problems you experience when packaging, deploying, or querying an app package.
ms.assetid: 38E327C6-0345-4FA6-BCDB-5FA2FCD421FB
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting packaging, deployment, and query of Windows Store apps

Use these suggestions to troubleshoot problems you experience when packaging, deploying, or querying an app package.

## Get diagnostic info

When an API fails, it returns an error code that describes the problem.

If the error code doesn't provide enough info, you can get detailed event logs that provide more info to help you diagnose the cause of the problem.

**To access the packaging and deployment event logs**

1.  Run **eventvwr.msc**.
2.  Go to **Event Viewer (Local)** > **Applications and Services Logs** > **Microsoft** > **Windows**.
3.  The first log to check is **AppxPackagingOM** > **Microsoft-Windows-AppxPackaging/Operational**.
4.  Deployment-related errors are recorded in **AppXDeployment-Server** > **Microsoft-Windows-AppXDeploymentServer/Operational**.

You can also use the following command in PowerShell to get the first few logged events:

**Get-Appxlog \| Out-GridView**

## Common error codes

This table lists the most common error codes.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Error code</th>
<th>Value</th>
<th>Description and possible causes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ERROR_BAD_FORMAT</strong></td>
<td>0x800700B</td>
<td>The package isn't correctly formatted and needs to be re-built or re-signed.<br/> You may get this error if there is a mismatch between the signing certificate subject name and the AppxManifest.xml publisher name.<br/> See [How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md).<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_OPEN_</strong><br/> <strong>PACKAGE_FAILED</strong><br/></td>
<td>0x80073CF0</td>
<td>The package couldn't be opened.<br/> Possible causes:<br/>
<ul>
<li>The package is unsigned.</li>
<li>The publisher name doesn't match the signing certificate subject.</li>
<li>The file:// prefix is missing or the package couldn't be found at the specified location.</li>
</ul>
Check the <strong>AppxPackagingOM</strong> event log for more info.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_PACKAGE_</strong><br/> <strong>NOT_FOUND</strong><br/></td>
<td>0x80073CF1</td>
<td>The package couldn't be found.<br/> You may get this error while removing a package that isn't installed for the current user.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_INVALID_</strong><br/> <strong>PACKAGE</strong><br/></td>
<td>0x80073CF2</td>
<td>The package data isn't valid.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_RESOLVE_</strong><br/> <strong>DEPENDENCY_FAILED</strong><br/></td>
<td>0x80073CF3</td>
<td>The package failed update, dependency, or conflict validation.<br/> Possible causes:<br/>
<ul>
<li>The incoming package conflicts with an installed package.</li>
<li>A specified package dependency can't be found.</li>
<li>The package doesn't support the correct processor architecture.</li>
</ul>
Check the <strong>AppXDeployment-Server</strong> event log for more info.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_OUT_</strong><br/> <strong>OF_DISK_SPACE</strong><br/></td>
<td>0x80073CF4</td>
<td>There isn't enough disk space on your computer. Free some space and try again.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_NETWORK_</strong><br/> <strong>FAILURE</strong><br/></td>
<td>0x80073CF5</td>
<td>The package can't be downloaded.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_</strong><br/> <strong>REGISTRATION_FAILURE</strong><br/></td>
<td>0x80073CF6</td>
<td>The package can't be registered.<br/> Check the <strong>AppXDeployment-Server</strong> event log for more info.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_</strong><br/> <strong>DEREGISTRATION_EFAILURE</strong><br/></td>
<td>0x80073CF7</td>
<td>The package can't be unregistered.<br/> You may get this error while removing a package.<br/> Check the <strong>AppXDeployment-Server</strong> event log for more info.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_CANCEL</strong></td>
<td>0x80073CF8</td>
<td>The user canceled the install request.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_FAILED</strong></td>
<td>0x80073CF9</td>
<td>Package install failed. Contact the software vendor.<br/> Check the <strong>AppXDeployment-Server</strong> event log for more info.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_REMOVE_FAILED</strong></td>
<td>0x80073CFA</td>
<td>Package removal failed.<br/> You may get this error for failures that occur during package uninstall.<br/> For more info, see <a href="https://msdn.microsoft.com/library/windows/apps/dn278489"><strong>RemovePackageAsync</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_PACKAGE_</strong><br/> <strong>ALREADY_EXISTS</strong><br/></td>
<td>0x80073CFB</td>
<td>The provided package is already installed, and reinstallation of the package is blocked. <br/> You may get this error if installing a package that is not bitwise identical to the package that is already installed. Note that the digital signature is also part of the package. Hence if a package is rebuilt or resigned, it is no longer bitwise identical to the previously installed package. Two possible options to fix this error are: (1) Increment the version number of the app, then rebuild and resign the package (2) Remove the old package for every user on the system before installing the new package. <br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_NEEDS_REMEDIATION</strong></td>
<td>0x80073CFC</td>
<td>The app can't be started. Try reinstalling the app.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_</strong><br/> <strong>PREREQUISITE_FAILED</strong><br/></td>
<td>0x80073CFD</td>
<td>A specified install prerequisite couldn't be satisfied.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_PACKAGE_</strong><br/> <strong>REPOSITORY_CORRUPTED</strong><br/></td>
<td>0x80073CFE</td>
<td>The package repository is corrupted.<br/> You may get this error if the folder referenced by this registry key doesn't exist or is corrupted: <br/> <strong>HKLM\Software\Microsoft\Windows\</strong><br/> <strong>CurrentVersion\Appx\PackageRepositoryRoot</strong><br/> To recover from this state, refresh your PC.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_INSTALL_</strong><br/> <strong>POLICY_FAILURE</strong><br/></td>
<td>0x80073CFF</td>
<td>To install this app, you need a developer license or a sideloading-enabled system. <br/> You may get this error if the package doesn't meet one of the following requirements:<br/>
<ul>
<li>The app is deployed using F5 in Visual Studio on a computer with a Windows Store developer license.</li>
<li>The package is signed with a Microsoft signature and deployed as part of Windows or from the Windows Store.</li>
<li>The package is signed with a trusted signature and installed on a computer with a Windows Store developer license, a domain-joined computer with the AllowAllTrustedApps policy enabled, or a computer with a Windows Sideloading license with the AllowAllTrustedApps policy enabled.</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>ERROR_PACKAGE_UPDATING</strong></td>
<td>0x80073D00</td>
<td>The app can't be started because it's currently updating.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_DEPLOYMENT_</strong><br/> <strong>BLOCKED_BY_POLICY</strong><br/></td>
<td>0x80073D01</td>
<td>The package deployment operation is blocked by policy. Contact your system administrator.<br/> Possible causes:<br/>
<ul>
<li>Package deployment is blocked by Application Control Policies.</li>
<li>Package deployment is blocked by the &quot;Allow deployment operations in special profiles&quot; policy.</li>
</ul>
One of the possible reasons is a need for a roaming profile. See <a href="https://msdn.microsoft.com/en-us/library/JJ649079(v=WS.11).aspx">Deploy Roaming User Profiles</a> to set up Roaming User Profiles on user accounts. If there are no policies configured on your system and you still see this error, perhaps you are logged in with a temporary profile. Log out and log in again, then try the operation again.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_PACKAGES_IN_USE</strong></td>
<td>0x80073D02</td>
<td>The package couldn't be installed because resources it modifies are currently in use.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_RECOVERY_</strong><br/> <strong>FILE_CORRUPT</strong><br/></td>
<td>0x80073D03</td>
<td>The package couldn't be recovered because data that's necessary for recovery is corrupted.<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INVALID_</strong><br/> <strong>STAGED_SIGNATURE</strong><br/></td>
<td>0x80073D04</td>
<td>The signature isn't valid. To register in developer mode, AppxSignature.p7x and AppxBlockMap.xml must be valid or shouldn't be present.<br/> If you are a developer using F5 with Visual Studio, ensure that your built project directory doesn't contain signature or block map files from previous versions of the package.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_DELETING_EXISTING_</strong><br/> <strong>APPLICATIONDATA_STORE_FAILED</strong><br/></td>
<td>0x80073D05</td>
<td>An error occurred while deleting the package's previously existing application data.<br/> You can get this error if the <a href="https://msdn.microsoft.com/en-us/library/Hh441475(v=VS.110).aspx">simulator</a> is running. Close the simulator. You can also get this error if there are files open in the app data (for example, if you have a log file open in a text editor).<br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_</strong><br/> <strong>PACKAGE_DOWNGRADE</strong><br/></td>
<td>0x80073D06</td>
<td>The package couldn't be installed because a higher version of this package is already installed.<br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_SYSTEM_</strong><br/> <strong>NEEDS_REMEDIATION</strong><br/></td>
<td>0x80073D07</td>
<td>An error in a system binary was detected. Try refreshing the PC to fix the problem. <br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_APPX_INTEGRITY_</strong><br/> <strong>FAILURE_EXTERNAL</strong><br/></td>
<td>0x80073D08</td>
<td>A corrupted non-Windows binary was detected on the system. <br/></td>
</tr>
<tr class="odd">
<td><strong>ERROR_RESILIENCY_</strong><br/> <strong>FILE_CORRUPT</strong><br/></td>
<td>0x80073D09</td>
<td>The operation couldn't be resumed because data that's necessary for recovery is corrupted. <br/></td>
</tr>
<tr class="even">
<td><strong>ERROR_INSTALL_FIREWALL_</strong><br/> <strong>SERVICE_NOT_RUNNING</strong><br/></td>
<td>0x80073D0A</td>
<td>The package couldn't be installed because the Windows Firewall service isn't running. Enable the Windows Firewall service and try again.<br/></td>
</tr>
<tr class="odd">
<td><strong>APPX_E_PACKAGING_INTERNAL</strong></td>
<td>0x80080200</td>
<td>The packaging API has encountered an internal error.<br/></td>
</tr>
<tr class="even">
<td><strong>APPX_E_INTERLEAVING_</strong><br/> <strong>NOT_ALLOWED</strong><br/></td>
<td>0x80080201</td>
<td>The package isn't valid because its contents are interleaved.<br/></td>
</tr>
<tr class="odd">
<td><strong>APPX_E_RELATIONSHIPS_</strong><br/> <strong>NOT_ALLOWED</strong><br/></td>
<td>0x80080202</td>
<td>The package isn't valid because it contains OPC relationships.<br/></td>
</tr>
<tr class="even">
<td><strong>APPX_E_MISSING_</strong><br/> <strong>REQUIRED_FILE</strong><br/></td>
<td>0x80080203</td>
<td>The package isn't valid because it's missing a manifest or block map, or a code integrity file is present but a signature file is missing.<br/> Ensure that the package isn't missing one or more of these required files:<br/>
<ul>
<li>\AppxManifest.xml</li>
<li>\AppxBlockMap.xml</li>
</ul>
If the package contains \AppxMetadata\CodeIntegrity.cat, it must also contain \AppxSignature.p7x.<br/></td>
</tr>
<tr class="odd">
<td><strong>APPX_E_INVALID_MANIFEST</strong></td>
<td>0x80080204</td>
<td>The package's AppxManifest.xml file isn't valid.<br/></td>
</tr>
<tr class="even">
<td><strong>APPX_E_INVALID_BLOCKMAP</strong></td>
<td>0x80080205</td>
<td>The package's AppxBlockMap.xml file isn't valid.<br/></td>
</tr>
<tr class="odd">
<td><strong>APPX_E_CORRUPT_CONTENT</strong></td>
<td>0x80080206</td>
<td>The package contents can't be read because it's corrupted.<br/></td>
</tr>
<tr class="even">
<td><strong>APPX_E_BLOCK_</strong><br/> <strong>HASH_INVALID</strong><br/></td>
<td>0x80080207</td>
<td>The computed hash value of the block doesn't match the has value stored in the block map.<br/></td>
</tr>
<tr class="odd">
<td><strong>APPX_E_REQUESTED_</strong><br/> <strong>RANGE_TOO_LARGE</strong><br/></td>
<td>0x80080208</td>
<td>The requested byte range is over 4 GB when translated to a byte range of blocks.<br/></td>
</tr>
<tr class="even">
<td><strong>TRUST_E_NOSIGNATURE</strong></td>
<td>0x800B0100</td>
<td>No signature is present in the subject.<br/> You may get this error if the package is unsigned or the signature isn't valid. The package must be signed to be deployed.<br/></td>
</tr>
<tr class="odd">
<td><strong>CERT_E_UNTRUSTEDROOT</strong></td>
<td>0x800B0109</td>
<td>A certificate chain processed, but terminated in a root certificate which isn't trusted by the trust provider.<br/> See <a href="https://msdn.microsoft.com/en-us/library/BR230260(v=VS.110).aspx">Signing a package</a>.<br/></td>
</tr>
<tr class="even">
<td><strong>CERT_E_CHAINING</strong></td>
<td>0x800B010A</td>
<td>A certificate chain couldn't be built to a trusted root certification authority.<br/> See <a href="https://msdn.microsoft.com/en-us/library/BR230260(v=VS.110).aspx">Signing a package</a>.<br/></td>
</tr>
<tr class="odd">
<td><strong>APPX_E_INVALID_</strong> <br/> <strong>SIP_CLIENT_DATA</strong> <br/></td>
<td>0x80080209</td>
<td>The <a href="https://msdn.microsoft.com/library/windows/desktop/bb736434"><strong>SIP_SUBJECTINFO</strong></a>structure used to sign the package didn't contain the required data<br/></td>
</tr>
<tr class="even">
<td><strong>E_INVALIDARG</strong></td>
<td>0x80070057</td>
<td>One or more arguments are not valid If you check the AppXDeployment-Server event log and see the following event;  While installing the package, the system failed to register the windows.repositoryExtension extension due to the following error: The parameter is incorrect. <br/> You may get this error if the manifest elements DisplayName or Description contain characters disallowed by Windows firewall; namely  |  and  all , due to which Windows fails to create the AppContainer profile for the package . Please remove these characters from the manifest and try installing the package. <br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[How to sign an app package using SignTool](how-to-sign-a-package-using-signtool.md)
</dt> <dt>

[How to troubleshoot app package signature errors](how-to-troubleshoot-app-package-signature-errors.md)
</dt> </dl>

 

 





