---
description: When accessing WMI local or remote data in an application or script, you may encounter errors ranging from missing classes to access denied. Providers also have debugging options and troubleshooting classes available.
ms.assetid: b0aecdf6-ec30-49be-af4e-7eac5d124057
ms.tgt_platform: multiple
title: WMI Troubleshooting
ms.topic: troubleshooting-general
ms.date: 09/25/2023
---

# WMI Troubleshooting

When accessing WMI local or remote data in an application or script, you might encounter errors ranging from missing classes to access denied. Providers also have debugging options and troubleshooting classes available.

> [!NOTE]  
> The info in this topic is intended for developers and IT administrators. If you're an end-user who has experienced an error message concerning WMI, then visit [Microsoft Support](https://support.microsoft.com/), and search for the error code that you see in the error message. For more info about troubleshooting problems with WMI scripts and the WMI service, see [WMI isn't working!](/previous-versions/tn-archive/ff406382(v=msdn.10))

## WMI Diagnosis Utility

> [!IMPORTANT]
> The WMI Diagnosis Utility (`WMIDiag.exe`) is no longer supported, starting with Windows 8 and Windows Server 2012.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:**  

If WMI returns error messages, be aware that they might not indicate problems in the WMI service or in WMI providers. Failures can originate in other parts of the operating system, and emerge as errors through WMI. Under no circumstances should you delete the WMI repository as a first step; because deleting the repository can cause damage to the system or to installed applications.

Previously, to obtain more info about the source of the problem, you could download and run the WMI Diagnosis Utility diagnostic command line tool. This tool produced a report that could usually isolate the source of the problem, and provide instructions on how to fix it. The report also aided Microsoft support services in assisting you. The WMI Diagnosis Utility was previously available at the Download Center.

As a provider writer, you might also encounter debugging issues unless you're writing a [*decoupled provider*](gloss-d.md). For more info, see [Debugging providers](debugging-providers.md).

## Logging and tracing

The WMI log files no longer exist; they were replaced by [Event Tracing for Windows (ETW)](/windows/desktop/ETW/event-tracing-portal). For more info, see [Tracing WMI activity](tracing-wmi-activity.md), [Logging WMI activity](logging-wmi-activity.md), and [WMI log files](wmi-log-files.md).

## Troubleshooting in scripts and applications

WMI contains a set of classes for [troubleshooting](wmi-troubleshooting-classes.md) client applications that use WMI providers. For more info, see [Troubleshooting WMI client applications](troubleshooting-wmi-client-applications.md).

## How provider-writers can prevent WMI problems

Provider-writers can prevent many problems (that appear in error messages through WMI) by performing the following actions:

* Registering your provider correctly. For more information, see [Registering a provider](registering-a-provider.md).
* Adding the [**\#pragma autorecover**](pragma-autorecover.md) statement to the Managed Object Format (MOF) file that defines your provider classes.

For more info, see [Debugging providers](debugging-providers.md), [Providing data to WMI](providing-data-to-wmi.md), and [Provider configuration and troubleshooting classes](provider-configuration-and-troubleshooting-classes.md).

## Access denied

*Access denied* errors that are reported by scripts and applications that access WMI namespaces and data generally fall into three categories. The following table lists the three categories of errors along with issues that might cause the errors and possible solutions.

| Error                                                                                                                        | Possible Issues                                                                                                                                                                                                                                                                                                                                                                     | Solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x800706BA `HRESULT_FROM_WIN32(RPC_S_SERVER_UNAVAILABLE)`<br/> Firewall issue or server not available.<br/>      | The computer really doesn't exist or the Windows Firewall is blocking the connection<br/>                                                                                                                                                                                                                                                                                        | Connecting to Vista: **netsh advfirewall firewall set rule group="windows management instrumentation (wmi)" new enable=yes** Connecting to downlevel: Allow the "Remote Administration" rule in Windows Firewall.<br/>                                                                                                                                                                                                                                                                                                            |
| 0x80070005 **E\_ACCESS\_DENIED**<br/> Access denied by DCOM security.<br/>                                       | The user does not have remote access to the computer through DCOM. Typically, DCOM errors occur when connecting to a remote computer with a different operating system version.<br/>                                                                                                                                                                                          | Give the user Remote Launch and Remote Activation permissions in dcomcnfg. Right-click My Computer-> Properties. Under COM Security, click "Edit Limits" for both sections. Give the user you want remote access, remote launch, and remote activation. Then go to DCOM Config, find "Windows Management Instrumentation", and give the user you want Remote Launch and Remote Activation. For more information, see [Connecting Between Different Operating Systems](/windows/desktop/WmiSdk/troubleshooting-a-remote-wmi-connection)<br/> |
| 0x80041003 **WBEM\_E\_ACCESS\_DENIED**<br/> Access denied by a [*provider*](gloss-p.md)<br/> | The user does not have permission to perform the operation in WMI. This could happen when you query certain classes as a low-rights user, but most often happens when you attempt to invoke methods or change WMI instances as a low rights user. The namespace you are connecting to is encrypted, and the user is attempting to connect with an unencrypted connection<br/> | Give the user access with the WMI Control (make sure they have Remote\_Access set to true) Connect using a client that supports encryption.<br/>                                                                                                                                                                                                                                                                                                                                                                                  |



 

-   Typically, DCOM errors occur when connecting to a remote computer with a different operating system version.

-   Providers may also deny access to data in specific namespaces or may require certain levels of connection security. For more information, see [Setting Client Application Process Security](setting-client-application-process-security.md) and [Provider Hosting and Security](provider-hosting-and-security.md).

-   Access denied errors from Internet Connection Firewall (ICF) changes.

    For more information, see [Connecting Through Windows Firewall](/windows/desktop/WmiSdk/connecting-to-wmi-remotely-starting-with-vista).

-   An access denied error is returned by DCOM security when a low-integrity client tries to access WMI. For example, an ActiveX control that is running in Internet Explorer, which has the security level set to low, does not have access to perform local WMI operations.

    **Windows 7:** Low-integrity users have read-only permissions for local WMI operations.

## Information on Errors

When you get an error message from WMI, you can locate the message in [**WMI Error Constants**](wmi-error-constants.md) or, for scripting, [**WbemErrorEnum**](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemerrorenum). However, the information supplied by the error alone is typically insufficient to determine what is happening. WMI repository corruption may masquerade as classes or instances "not found".

For more information about WMI errors:

-   The WMI logs track events from within the WMI core and from providers. For more information, see [Logging WMI Activity](logging-wmi-activity.md).
-   Use the [WMI Troubleshooting Classes](wmi-troubleshooting-classes.md) to check WMI internal status or receive notifications of provider or WMI service events. For more information, see [Provider Configuration and Troubleshooting Classes](provider-configuration-and-troubleshooting-classes.md) and [Troubleshooting WMI Client Applications](troubleshooting-wmi-client-applications.md).

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[Tracing WMI Activity](tracing-wmi-activity.md)
</dt> <dt>

[Logging WMI Activity](logging-wmi-activity.md)
</dt> </dl>

 

