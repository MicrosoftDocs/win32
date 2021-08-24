---
description: In Windows 7, WMI implemented the Win32\_OptionalFeature class. This class retrieves the status of the optional features that are present on a computer.
ms.assetid: d756b0c0-b9f4-4b71-9f07-963a0dd5e585
ms.tgt_platform: multiple
title: Querying the Status of Optional Features
ms.topic: article
ms.date: 05/31/2018
---

# Querying the Status of Optional Features

In Windows 7, WMI implemented the [**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature) class. This class retrieves the status of the optional features that are present on a computer.

You can use Windows PowerShell cmdlets to query the status of optional features. All of the examples in this topic use the Get-WmiObject cmdlet. For more information, see [Get-WmiObject](/previous-versions//dd315295(v=technet.10)).

**To retrieve all instances of optional features present on a computer**


    
| PowerShell | 
|------------|
| <pre><code>Get-WmiObject Win32_OptionalFeature</code></pre> | 


    

**To query for an optional feature by specifying the feature name**


    
| PowerShell | 
|------------|
| <pre><code>Get-WmiObject -query "select * from Win32_OptionalFeature where name = 'TelnetClient'"</code></pre> | 


    

    > [!Note]  
    > The **name** property is case-sensitive.

     

**To query for optional features by specifying the install state**


    
| PowerShell | 
|------------|
| <pre><code>Get-WmiObject -query "select * from win32_optionalfeature where installstate= 1"</code></pre> | 


    

    For more information about the possible values for the **InstallState** property, see [**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature).

## Related topics

<dl> <dt>

[**Win32\_OptionalFeature**](/windows/desktop/CIMWin32Prov/win32-optionalfeature)
</dt> </dl>

 

 
