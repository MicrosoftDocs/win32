---
description: WMI providers also may maintain logs. Which log files appear on a system depends on which providers are installed.
ms.assetid: 04f041e5-4f2c-4c94-9aba-b040d941b46d
ms.tgt_platform: multiple
title: WMI Provider Log Files
ms.topic: article
ms.date: 05/31/2018
---

# WMI Provider Log Files

WMI providers also may maintain logs. Which log files appear on a system depends on which providers are installed.

These logs may be located in the %systemroot%\\system32\\wbem\\logs directory.

-   [Wmiprov.log](#wmiprovlog)
-   [Ntevt.log](#ntevtlog)
-   [Dsprovider.log](#dsproviderlog)
-   [Related topics](#related-topics)

## Wmiprov.log

The Wmiprov.log file contains management data and events from WMI-enabled Windows Driver Model (WDM) drivers and the [WDM Provider](/windows/desktop/WmiCoreProv/wdm-provider). It supplies warning and error information primarily for troubleshooting and debugging the provider and client applications that use it.

The Wmiprov.log contains:

-   Errors from the [WDM Provider](/windows/desktop/WmiCoreProv/wdm-provider) or the device driver such as the binary MOF compile failing or failure to retrieve data.
-   The status of the MOF compile for each of the drivers which use MOF format.
-   Provider construction and deconstruction events.
-   Printout of WNODE.

## Ntevt.log

The Ntevt.log file contains trace messages from the [Event Log Provider](/previous-versions/windows/desktop/eventlogprov/event-log-provider).

## Dsprovider.log

The Dsprovider.log file contains trace information and error messages for the [Active Directory Provider](/previous-versions/windows/desktop/dsprov/active-directory-provider).

The following table lists some common problems that can occur and offers possible causes and solutions.



| Message                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CLDAPClassProvider::InitializeLDAPProvider ADsGetObject on RootDSE FAILED : &lt;hresult&gt;                                                                                                                                                                                                                    | The ADSI call failed while trying to get the root of your directory services. Verify that your computer is a member of a domain.                                                                                                                                                                                                                                                                             |
| CDSClassProvider::GetObjectAsync() GetClassFromCacheOrADSI FAILED for \<class name> with &lt;hresult&gt;                                                                                                                                                                                                  | The class you are trying to get is not a valid class in the directory. Verify that the class name is correct.                                                                                                                                                                                                                                                                                                |
| CLDAPInstanceProvider::PutInstanceAsync() ModifyExistingInstance FAILED for LDAP://CN=foo1, CN=Users, DC=dsprovider,DC=nttest, DC=Microsoft, DC=com with &lt;hresult&gt;                                                                                                                                       | The provider was unable to write a modified instance to directory services. Ensure that you are using the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) interface to specify the set of properties that you are modifying. For more information about how to use the **IWbemContext** interface with [**PutInstance**](/windows/desktop/api/Provider/nf-provider-provider-putinstance(constcinstance__long)), see [Updating an Entire Instance](updating-an-entire-instance.md). |
| CLDAPHelper::GetADSIInstance ADsOpenObject() FAILED on \<class name> with &lt;hresult&gt;<br/> CLDAPInstanceProvider::GetObjectAsync : GetADSIInstance() FAILED with &lt;hresult&gt;<br/> CLDAPInstanceProvider::GetObjectAsync() FAILED for ds\_user.ADSIPath="\<class name><br/> | These three messages indicate that the instance you are trying to get does not exist in the directory service. Verify that the **ADSIPath** value and class name are correct.                                                                                                                                                                                                                                |



 

## Related topics

<dl> <dt>

[WMI Log Files](wmi-log-files.md)
</dt> </dl>

 

