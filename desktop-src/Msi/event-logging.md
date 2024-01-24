---
description: Windows Events provides a standard, centralized way for applications (and the operating system) to record important software and hardware events.
ms.assetid: 1f28cbce-b759-4293-8af2-15f86f23228c
title: Event Logging (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Event Logging (Windows Installer)

[Windows Events](../events/windows-events.md) provides a standard, centralized way for applications (and the operating system) to record important software and hardware events. The event-logging service stores events from various sources in a single collection called an *event log*. Prior to Windows Vista, you would use either [Event Tracing for Windows](../etw/event-tracing-portal.md) (ETW) or [Event Logging](../eventlog/event-logging.md) to log events. Windows Vista introduced a new eventing model that unifies both ETW and the [Windows Event Log](../wes/windows-event-log.md) API.

The installer also writes entries into the event log. These record events such as following:

-   Success or failure of the installation; removal or repair of a product.
-   Errors that occur during product configuration.
-   Detection of corrupted configuration data.

If a large amount of information is written, the Event Log file can become full and the installer displays the message, "The Application log file is full."

The installer may write the following entries in the event log. All event log messages have a unique event ID. All general errors authored in the [Error table](error-table.md) that are returned for an installation that fails are logged in the Application Event Log with a message ID equal to the Error + 10,000. For example, the error number in the Error table for an installation completed successfully is 1707. The successful installation is logged in the Application Event Log with a message ID of 11707 (1707 + 10,000).

For information about how to enable verbose logging on a user's computer when troubleshooting deployment, see [Windows Installer Best Practices](windows-installer-best-practices.md).



<table>
<thead>
<tr class="header">
<th>Event ID</th>
<th>Message</th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1001</td>
<td>Detection of product '%1', feature '%2' failed during request for component '%3'</td>
<td>A warning message. For details, see <a href="searching-for-a-broken-feature-or-component.md">Searching For a Broken Feature or Component</a>.</td>
</tr>
<tr class="even">
<td>1002</td>
<td>Unexpected or missing value (name: '%1', value: '%2') in key '%3'</td>
<td>Error message that there was an unexpected or missing value.</td>
</tr>
<tr class="odd">
<td>1003</td>
<td>Unexpected or missing subkey '%1' in key '%2'</td>
<td>Error message that there was an unexpected or missing subkey.</td>
</tr>
<tr class="even">
<td>1004</td>
<td>Detection of product '%1', feature '%2', component '%3' failed <strong>Note:</strong> Beginning with Windows Installer version 2.0, this message is: Detection of product '%1', feature '%2', component '%3' failed. The resource '%4' does not exist.<br/></td>
<td>A warning message. See also <a href="searching-for-a-broken-feature-or-component.md">Searching For a Broken Feature or Component</a>.</td>
</tr>
<tr class="odd">
<td>1005</td>
<td>Install operation initiated a reboot</td>
<td>Informational message that the installation initiated a reboot of the system.</td>
</tr>
<tr class="even">
<td>1006</td>
<td>Verification of the digital signature for cabinet '%1' cannot be performed. WinVerifyTrust is not available on the computer.</td>
<td>Warning message. A cabinet was authored in the <a href="msidigitalsignature-table.md">MsiDigitalSignature table</a> to have a <a href="/windows/desktop/api/wintrust/nf-wintrust-winverifytrust"><strong>WinVerifyTrust</strong></a> check performed. This action could not be performed because the computer does not have the proper cryptography DLLs installed.</td>
</tr>
<tr class="odd">
<td>1007</td>
<td>The installation of %1 is not permitted by software restriction policy. The Windows Installer only allows execution of unrestricted items. The authorization level returned by software restriction policy was %2.</td>
<td>An error message indicating that the administrator has configured software restriction policy to disallow this install.</td>
</tr>
<tr class="even">
<td>1008</td>
<td>The installation of %1 is not permitted due to an error in software restriction policy processing. The object cannot be trusted.</td>
<td>An error message indicating that there were problems attempting to verify the package according to software restriction policy.</td>
</tr>
<tr class="odd">
<td>1012</td>
<td>This version of Windows does not support deploying 64-bit packages. The script '%1' is for a 64-bit package.</td>
<td>Error message indicating that scripts for 64-bit packages can only be executed on a 64-bit computer.</td>
</tr>
<tr class="even">
<td>1013</td>
<td>{Unhandled exception report}</td>
<td>Error message for an unhandled exception, this is the report.</td>
</tr>
<tr class="odd">
<td>1014</td>
<td>Windows Installer proxy information not registered correctly</td>
<td>Error message that proxy information was not registered correctly.</td>
</tr>
<tr class="even">
<td>1015</td>
<td>Failed to connect to server. Error: %d</td>
<td>Informational message that the installation failed to connect to server.</td>
</tr>
<tr class="odd">
<td>1016</td>
<td>Detection of product '%1', feature '%2', component '%3' failed. The resource '%4' in a run-from-source component could not be located because no valid and accessible source could be found.</td>
<td>Warning message. For more information, see <a href="searching-for-a-broken-feature-or-component.md">Searching for a Broken Feature or Component</a>.</td>
</tr>
<tr class="even">
<td>1017</td>
<td>User SID had changed from '%1' to '%2' but the managed app and the user data keys cannot be updated. Error = '%3'.</td>
<td>Error message indicating that an error occurred while attempting to update the user's registration after the user's SID changed.</td>
</tr>
<tr class="odd">
<td>1018</td>
<td>The application '%1' cannot be installed because it is not compatible with this version of Windows.</td>
<td>Error message indicating that the installation is incompatible with the currently running version of Windows. Contact the manufacturer of the software being installed for an update.</td>
</tr>
<tr class="even">
<td>1019</td>
<td>Product: %1 - Update '%2' was successfully removed.</td>
<td>Informational message that the installer has removed the update.<strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1020</td>
<td>Product: %1 - Update '%2' could not be removed. Error code %3. Additional information is available in the log file %4.</td>
<td>Error message indicating that the installer was unable to remove the update. Additional information is available in the log file.<strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1021</td>
<td>Product: %1 - Update '%2' could not be removed. Error code %3.</td>
<td>Error message indicating that the installer was unable to remove the update. For information on how to turn on logging, see <a href="windows-installer-best-practices.md">Enable verbose logging on user's computer when troubleshooting deployment.</a><strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1022</td>
<td>Product: %1 - Update '%2' installed successfully.</td>
<td>Informational message that the installer has installed the update successfully. <strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1023</td>
<td>Product: %1 - Update '%2' could not be installed. Error code %3. Additional information is available in the log file %4.</td>
<td>Error message indicating that the installer was unable to install the update. Additional information is available in the log file.<strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1024</td>
<td>Product: %1 - Update '%2' could not be installed. Error code %3.</td>
<td>Error message indicating that the installer was unable to install the update. For information on how to turn logging on, see <a href="windows-installer-best-practices.md">Enable verbose logging on user's computer when troubleshooting deployment.</a><strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1025</td>
<td>Product: %1. The file %2 is being used by the following process: Name: %3 , Id %4.</td>
<td><strong>Windows Installer 2.0:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1026</td>
<td>Windows Installer has determined that its configuration data registry key was not secured properly. The owner of the key must be either Local System or Builtin\Administrators. The existing key will be deleted and re-created with the appropriate security settings.</td>
<td>Warning message.<strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1027</td>
<td>Windows Installer has determined that a registry sub key %1 within its configuration data was not secured properly. The owner of the key must be either Local System or Builtin\Administrators. The existing sub key and all of its contents will be deleted.</td>
<td>Warning message.<strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1028</td>
<td>Windows Installer has determined that its configuration data cache folder was not secured properly. The owner of the key must be either Local System or Builtin\Administrators. The existing folder will be deleted and re-created with the appropriate security settings.</td>
<td>Warning message<strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1029</td>
<td>Product: %1. Restart required.</td>
<td>Warning message indicatiing that a system restart is required to complete the installation and the restart has been deferred to a later time.<strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1030</td>
<td>Product: %1. The application tried to install a more recent version of the protected Windows file %2. You may need to update your operating system for this application to work correctly. (Package Version: %3, Operating System Protected Version: %4).</td>
<td>Warning message indicating that the installation tried to replace a critical file that is protected by <a href="windows-resource-protection-on-windows-vista.md">Windows Resource Protection</a>. An update of the operating system may be required to use this application. <strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1031</td>
<td>Product: %1. The assembly '%2' for component '%3' is in use.</td>
<td>Warning message indicating that the installation tried to update an assembly currently in use. The system must be restarted to complete the update of this assembly.<strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="odd">
<td>1032</td>
<td>An error occurred while refreshing environment variables updated during the installation of '%1'.</td>
<td>Warning message indicating that some users who are logged on to the computer may need to log off and back on to complete the update of environment variables.<strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/></td>
</tr>
<tr class="even">
<td>1033</td>
<td>Product: %1. Version: %2. Language: %3. Installation completed with status: %4. Manufacturer: %5.</td>
<td>Field 1 - <a href="productname.md"><strong>ProductName</strong></a> Field 2 - <a href="productversion.md"><strong>ProductVersion</strong></a><br/> Field 3 - <a href="productlanguage.md"><strong>ProductLanguage</strong></a><br/> <strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/> Field 5 - <a href="manufacturer.md"><strong>Manufacturer</strong></a><br/> <strong><a href="not-supported-in-windows-installer-4-5.md">Windows Installer 4.5 and earlier</a>:</strong> Field 5 not available.<br/></td>
</tr>
<tr class="odd">
<td>1034</td>
<td>Product: %1. Version: %2. Language: %3. Removal completed with status: %4. Manufacturer: %5.</td>
<td>Field 1 - <a href="productname.md"><strong>ProductName</strong></a> Field 2 - <a href="productversion.md"><strong>ProductVersion</strong></a><br/> Field 3 - <a href="productlanguage.md"><strong>ProductLanguage</strong></a><br/> <strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/> Field 5 - <a href="manufacturer.md"><strong>Manufacturer</strong></a><br/> <strong><a href="not-supported-in-windows-installer-4-5.md">Windows Installer 4.5 and earlier</a>:</strong> Field 5 not available.<br/></td>
</tr>
<tr class="even">
<td>1035</td>
<td>Product: %1. Version: %2. Language: %3. Configuration change completed with status: %4. Manufacturer: %5.</td>
<td>Field 1 - <a href="productname.md"><strong>ProductName</strong></a> Field 2 - <a href="productversion.md"><strong>ProductVersion</strong></a><br/> Field 3 - <a href="productlanguage.md"><strong>ProductLanguage</strong></a><br/> Field 5 - <a href="manufacturer.md"><strong>Manufacturer</strong></a><br/> <strong><a href="not-supported-in-windows-installer-4-5.md">Windows Installer 4.5 and earlier</a>:</strong> Field 5 not available.<br/></td>
</tr>
<tr class="odd">
<td>1036</td>
<td>Product: %1. Version: %2. Language: %3. Update: %4. Update installation completed with status: %5. Manufacturer: %6.</td>
<td>Field 1 - <a href="productname.md"><strong>ProductName</strong></a> Field 2 - <a href="productversion.md"><strong>ProductVersion</strong></a><br/> Field 3 - <a href="productlanguage.md"><strong>ProductLanguage</strong></a><br/> Field 4 - This is the user friendly name if the <a href="msipatchmetadata-table.md">MsiPatchMetadata Table</a> is present in the patch package. Otherwise, this is the patch code GUID of the patch.<br/> Field 5 - Status of update installation.<br/> <strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/> Field 6 - <a href="manufacturer.md"><strong>Manufacturer</strong></a><br/> <strong><a href="not-supported-in-windows-installer-4-5.md">Windows Installer 4.5 and earlier</a>:</strong> Field 6 not available.<br/></td>
</tr>
<tr class="even">
<td>1037</td>
<td>Product: %1. Version: %2. Language: %3. Update: %4. Update removal completed with status: %5. Manufacturer: %6.</td>
<td>Field 1 - <a href="productname.md"><strong>ProductName</strong></a> Field 2 - <a href="productversion.md"><strong>ProductVersion</strong></a><br/> Field 3 - <a href="productlanguage.md"><strong>ProductLanguage</strong></a><br/> Field 4 - This is the user friendly name if the <a href="msipatchmetadata-table.md">MsiPatchMetadata Table</a> is present in the patch package. Otherwise, this is the patch code GUID of the patch.<br/> Field 5 - Status of update removal.<br/> <strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/> Field 6 - <a href="manufacturer.md"><strong>Manufacturer</strong></a><br/> <strong><a href="not-supported-in-windows-installer-4-5.md">Windows Installer 4.5 and earlier</a>:</strong> Field 6 not available.<br/></td>
</tr>
<tr class="odd">
<td>1038</td>
<td>Product: %1. Version: %2. Language: %3. Reboot required. Reboot Type: %4. Reboot Reason: %5. Manufacturer: %6.</td>
<td>Field 1 - <a href="productname.md"><strong>ProductName</strong></a> Field 2 - <a href="productversion.md"><strong>ProductVersion</strong></a><br/> Field 3 - <a href="productlanguage.md"><strong>ProductLanguage</strong></a><br/> <dl> Field 4 - A constant indicating the type of restart: <br/> <dl> <strong>msirbRebootImmediate</strong> (1) - There was an immediate restart of the computer.<br />
<strong>msirbRebootDeferred</strong> (2) - A user or admin has deferred a required restart of the computer using the UI or <a href="reboot.md"><strong>REBOOT</strong></a>=ReallySuppress.<br />
</dl> </dd> Field 5 - A constant indicating the reason for the restart:<br/> <dl> <strong>msirbRebootUndeterminedReason</strong> (0)- Restart required for an unspecified reason.<br />
<strong>msirbRebootInUseFilesReason</strong> (1)- A restart was required to replace files in use.<br />
<strong>msirbRebootScheduleRebootReason</strong> (2)- The package contains a <a href="schedulereboot-action.md">ScheduleReboot</a> action.<br />
<strong>msirbRebootForceRebootReason</strong> (3)- The package contains a <a href="forcereboot-action.md">ForceReboot</a> action.<br />
<strong>msirbRebootCustomActionReason</strong> (4)- A custom action called the <a href="/windows/desktop/api/Msiquery/nf-msiquery-msisetmode"><strong>MsiSetMode</strong></a> function.<br />
</dl> </dd> </dl> <strong><a href="not-supported-in-windows-installer-version-3-1.md">Windows Installer 3.1 and earlier</a>:</strong> Not available.<br/> Field 6 - <a href="manufacturer.md"><strong>Manufacturer</strong></a><br/> <strong><a href="not-supported-in-windows-installer-4-5.md">Windows Installer 4.5 and earlier</a>:</strong> Field 6 not available.<br/></td>
</tr>
<tr class="odd">
<td>1044</td>
<td>%1 is not Microsoft signed. So, rejecting per the Windows Lockdown Policy.</td>
<td>Error message indicating that binary is not signed by Microsoft and is not allowed as per Windows Lockdown Policy.</td>
</tr>
<tr class="even">
<td>10005</td>
<td>The installer has encountered an unexpected error installing this package. This may indicate a problem with this package. The error code is [1]. {{The arguments are: [2], [3], [4]}}</td>
<td>Error message indicating an internal error occurred. The text of this message is based upon the text authored for error 5 in the Error table.</td>
</tr>
<tr class="odd">
<td>11707</td>
<td>Product [2] – Installation operation completed successfully</td>
<td>Informational message that the installation of the product was successful.</td>
</tr>
<tr class="even">
<td>11708</td>
<td>Product [2] – Installation operation failed</td>
<td>Error message that the installation of the product failed.</td>
</tr>
<tr class="odd">
<td>11728</td>
<td>Product [2] -- Configuration completed successfully.</td>
<td>Informational message that configuration of the product was successful.</td>
</tr>
</tbody>
</table>



 

You can import localized errors strings for events into your database by using Msidb.exe or [**MsiDatabaseImport**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabaseimporta). The SDK includes localized resource strings for each of the languages listed in the [Localizing the Error and ActionText Tables](localizing-the-error-and-actiontext-tables.md) section. If the error strings corresponding to events are not populated, the installer loads localized strings for the language specified by the [**ProductLanguage**](productlanguage.md) property.

 

 
