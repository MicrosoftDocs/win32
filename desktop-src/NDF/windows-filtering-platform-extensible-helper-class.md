---
title: Windows Filtering Platform Extensible Helper Class
description: The Windows Filtering Platform (WFP) includes a Network Diagnostics Framework (NDF) helper class, called the Filtering Platform helper class (FPHC).
ms.assetid: 006ea30c-8682-4a3d-803a-73dba5162696
ms.topic: article
ms.date: 05/31/2018
---

# Windows Filtering Platform Extensible Helper Class

The [Windows Filtering Platform (WFP)](/windows/desktop/FWP/windows-filtering-platform-start-page) includes a Network Diagnostics Framework (NDF) helper class, called the Filtering Platform helper class (FPHC). FPHC can help identify the root causes of connectivity issues caused by WFP. Third-party firewall developers can implement their own NDF helper classes. FPHC extensibility allows these third-party helper classes to be invoked during diagnostics.

This topic assumes familiarity with the [WFP API](/windows/desktop/FWP/windows-filtering-platform-start-page).

## Why Extend the FPHC?

All developers that write applications that call the WFP API should write an NDF helper class that extends FPHC.

FPHC can identify WFP as the cause of a connectivity issue. If available, FPHC can also identify the provider that created the filter that is blocking network traffic. FPHC passes this information to NDF, which in turn can then notify the user that WFP is causing the connectivity problem and give the name of the provider blocking traffic.

However, the FPHC cannot suggest a corrective action to the user, nor can it provide the reason that the filter is blocking traffic to the user. Only a FPHC extension can perform those tasks.

Consider a third-party firewall application that calls the WFP API. If the third-party firewall implements a FPHC extension, then custom actions can be implemented to handle connectivity issues identified by NDF. When NDF diagnoses that an application has been blocked by the third-party firewall, the FPHC extension can handle the blocking event. One way that the FPHC extension could handle an event is to present the user with a prompt to unblock a program using the firewall and then unblock the program upon user confirmation. Alternatively, the FPHC extension could handle an event by notifying the user of the reason why the application was blocked, such as an application was blocked because it was considered malware by the firewall.

## About WFP Diagnostics

When NDF is invoked to diagnose a network issue, helper classes are contacted to determine the cause of the issue. If a higher-level helper class determines that a network failure may be caused by WFP, it generates a hypothesis for FPHC based on available information. NDF passes this hypothesis, in the form of several event attributes, to FPHC. These attributes are described in detail in the [FPHC Event Attributes](#windows-filtering-platform-extensible-helper-class) section below.

A network issue can be described as a connectivity problem affecting a particular connection attempt. For example, the user may have accidentally blocked an application by inadvertently clicking **Don't allow**. The firewall will then block the application from binding to any port. The user, not knowing why the application is blocked, may try to diagnose the issue through an entry point offered by the application. FPHC will look at the logs, and if it finds a match it will retrieve the filter ID and the provider ID of that particular filter. At this point, FPHC knows who the owner of that filter is, and it will hand over the diagnostic process to the appropriate helper class for further diagnosis.

The most recent event in the WFP event logs to match the attributes is selected as being relevant to the network issue. If no matching events are found and the time the event happened is covered in the WFP log, FPHC indicates to NDF that it is healthy. If no matching events are found and the WFP logs do not include the time the event occurred, FPHC returns an indeterminate status to NDF.

If a matching event is found, FPHC uses the provider ID of the filter which caused the event to identify the provider of the security rule that blocked connectivity. FPHC then checks whether a helper class extension exists for that provider. If one is found, FPHC generates a hypothesis for that provider and then NDF invokes the extension. The extension should return helpful diagnostic and repair information to the user.

## Helper Class Registration

A FPHC extension must be registered as described in [Registering NDF Helper Class Extensions](registering-ndf-helper-class-extensions.md). Developers implementing a helper class must register their extensions to ensure that the extension is called by NDF when appropriate. The *matching attribute* described below must be stored in the registry under **HKLM\\System\\CurrentControlSet\\Control\\NetDiagFx**\\*VendorName*\\**HostDLLs**\\*Helper Class DLL*\\**HelperClasses**\\*Helper Class Name*\\**MatchAttributes**.

The following table shows the matching attribute used to identify the hypothesis to use in diagnostics in the WFP event log. 

| Name       | Type    | Description                                                                                                                                                                                                                                                                                                 |
|------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ProviderID | REG\_SZ | The GUID of the FPHC extension. This value must be the same as the WFP Provider GUID. <br/> This string is case-sensitive. It should be stored in the registry in upper case with enclosing braces and hyphens. For example, {C200E360-38C5-11CE-AE62-08002B2B79EF} is a valid ProviderID.<br/> |



 

When the ProviderID of a blocking filter matches that of a registered helper class, FPHC informs NDF to invoke that helper class, thus extending the diagnostic capability of FPHC.

## FPHC Event Attributes

The following table lists the event attributes associated with each matching event. Each event attribute is stored in a [**HELPER\_ATTRIBUTE**](/windows/win32/api/ndattrib/ns-ndattrib-helper_attribute) structure. These attributes are passed by NDF to FPHC when a matching event is found. These can in turn be passed to FPHC extensions.



| Attribute     | [**ATTRIBUTE\_TYPE**](/windows/win32/api/ndattrib/ne-ndattrib-attribute_type) value | Description                                                                                                                               |
|---------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Provider GUID | AT\_GUID                                        | The GUID of the provider associated with the filter.                                                                                      |
| Timestamp     | AT\_OCTET\_STRING                               | A buffer of type FILETIME that specifies the time at which the event occurred. This time stamp can be used to uniquely identify an event. |
| ipProtocol    | AT\_UINT32                                      | The transport layer protocol, in UINT8 format.                                                                                            |
| LocalAddr     | AT\_SOCKADDR                                    | The local IP address and port, stored in a [**DIAG\_SOCKADDR**](/windows/win32/api/ndattrib/ns-ndattrib-diag_sockaddr) structure.                                             |
| RemoteAddr    | AT\_SOCKADDR                                    | The remote IP address and port, stored in a [**DIAG\_SOCKADDR**](/windows/win32/api/ndattrib/ns-ndattrib-diag_sockaddr) structure.                                            |
| userId        | AT\_OCTET\_STRING                               | A buffer of type SID that represents the userid. If userId is of length 0, the SID is unavailable.                                        |
| appId         | AT\_STRING                                      | A buffer that stores the retrieved application identifier. If appId has a value of L"", the application identifier is unavailable.        |



 

## Handling FPHC Events

Before suggesting diagnostic and repair information to the user, a FPHC extension should gather more data than is provided by the FPHC notifications. This data can be acquired from the [WFP Event Management Functions](/windows/desktop/FWP/fwp-mgmt-functions). These functions are demonstrated in the [Displaying Net Events](/windows/desktop/FWP/displaying-net-events) sample.

A more detailed event management sample is included in the SDK. The source code for the sample can be found in the SDK installation location under C:\\Program Files\\Microsoft SDKs\\Windows\\\<version number\>\\Samples\\NetDs\\WFP\\DiagEvents. The Windows Vista SDK is available from the [Download Center](https://www.microsoft.com/downloads/details.aspx?FamilyID=f26b1aa4-741a-433a-9be5-fa919850bdbf).

## Built-in FPHC Diagnostics

In the absence of an FPHC extension, FPHC can diagnose the scenarios listed below. Most connectivity failures diagnosed by FPHC occur because firewalls block traffic. The IPsec scenarios are less common.

The following table shows some scenarios causing connectivity failures that can be diagnosed by FPHC, along with the description and repair information passed to NDF.



| Scenario                   | Low health description                                                                                                               | Repair information                   |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| Firewall drop              | The firewall settings on this computer are blocking the connection.                                                                  | Verify your firewall settings.       |
| Main Mode Failure          | You cannot connect because of an IPsec security policy mismatch.                                                                     | Contact the IPsec policy owner.      |
| Quick Mode Failure         | You cannot connect because of an IPsec security policy mismatch.                                                                     | Contact the IPsec policy owner.      |
| User Mode Failure          | You cannot connect because of an IPsec security policy mismatch.                                                                     | Contact the IPsec policy owner.      |
| Credential Failure         | You cannot connect because the root certification authority (CA) on this computer does not match the root CA on the remote computer. | Update the trusted root certificate. |
| Expired Certificate        | The certificate used for IPsec authentication has expired.                                                                           | Request a certificate.               |
| Other certificate failures | A valid certificate was not found for IPsec authentication.                                                                          | Request a certificate.               |
| Kerberos failure           | The computer is not part of this domain.                                                                                             | Join this computer to a domain.      |
| Preshared Key              | Reset the preshared keys.                                                                                                            | Reset the preshared keys.            |



 

## Related topics

<dl> <dt>

[Windows Filtering Platform](/windows/desktop/FWP/windows-filtering-platform-start-page)
</dt> <dt>

[Designing NDF Helper Class Extensions](designing-ndf-helper-class-extensions.md)
</dt> <dt>

[Registering NDF Helper Class Extensions](registering-ndf-helper-class-extensions.md)
</dt> <dt>

[NDF Helper Class Examples](ndf-helper-class-examples.md)
</dt> </dl>

 

