---
Description: The fax device provider node represents a single device provider.
ms.assetid: 9545a984-1b18-4aec-9401-906031e8ae9e
title: Fax Device Provider Node
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Device Provider Node

The fax device provider node represents a single device provider.

## When to Extend This Node

Extend this node if you must qualify behavior that is related to an fax service provider (FSP) at a global level, or if you must add properties that apply to all the fax devices that an FSP exposes.

> [!Note]  
> Use the [**FaxExtSetData**](/windows/previous-versions/FaxExt/nf-faxext-faxextsetdata?branch=master) function to set configuration data for a specific device and GUID.

 

## Node-Type GUID

{BD38E2AC-B926-4161-8640-0F6956EE2BA3}

## IDataObject Content

Use the following custom clipboard formats to retrieve information related to the fax device node.



| Clipboard format           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CF\_MSFAXSRV\_FSP\_GUID    | **Data format:** A null-terminated Unicode character string that contains a string representation of the GUID for the FSP. The string has the same format as the string returned by the Microsoft Win32 function [StringFromGUID2](http://msdn.microsoft.com/en-us/library/ms683893.aspx). An example of the string is {c200e360-38c5-11ce-ae62-08002b2b79ef}.<br/> **Remarks:** The maximum length of the GUID string, including the terminating null character, is FAXSRV\_MAX\_GUID\_LEN characters. FSPs registered using the Windows 2000 Fax Service Client API will get the Fax Service Provider name instead of the GUID.<br/> |
| CF\_MSFAXSRV\_SERVER\_NAME | **Data format:** A null-terminated Unicode character string that specifies the name of the fax server with which the provider is associated. The server name is not preceded by "\\\\".<br/> **Remarks:** The maximum length of the server name string, including the terminating null character, is FAXSRV\_MAX\_SERVER\_NAME characters.<br/>                                                                                                                                                                                                                                                                                        |



 

 

 




