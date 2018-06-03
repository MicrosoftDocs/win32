---
title: Script Complex Type
description: Specifies the script to run.
ms.assetid: 0a339a47-ee09-4da3-9b7b-b42454c3c0b0
keywords:
- Script complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Script
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Script Complex Type

Specifies the script to run.

``` syntax
<xs:complexType name="Script">
    <xs:sequence>
        <xs:element name="Parameters"
            type="dcmPS:Parameters"
            minOccurs="0"
            maxOccurs="1"
        >
            <xs:unique name="No_script_parameters_may_have_the_same_name">
                <xs:selector
                    xpath="Parameter"
                 />
                <xs:field
                    xpath="Name"
                 />
            </xs:unique>
        </xs:element>
        <xs:element name="ProcessArchitecture"
            type="dcmPS:ProcessArchitecture"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="RequiresElevation"
            type="xs:boolean"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="RequiresInteractivity"
            type="xs:boolean"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="FileName"
            type="dcmPS:Name"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="ExtensionPoint"
            type="dcmPS:ExtensionPoint"
            minOccurs="0"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element               | Type                                                                        | Description                                                                                                                                               |
|-----------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtensionPoint        | [**dcmPS:ExtensionPoint**](package-extensionpoint-complextype.md)          | Used by the client to extend the functionality of the Script node. The MSDT client does not support extensions for the Script node. <br/>           |
| FileName              | [**dcmPS:Name**](package-name-simpletype.md)                               | The name of the script to run.<br/>                                                                                                                 |
| Parameters            | [**dcmPS:Parameters**](package-parameters-complextype.md)                  | Arguments to pass to the script.<br/>                                                                                                               |
| ProcessArchitecture   | [**dcmPS:ProcessArchitecture**](package-processarchitecture-simpletype.md) | The architecture on which the script can run. Should be set to ANY unless you have specific dependencies on 32-bit or 64-bit tools.<br/>            |
| RequiresElevation     | xs:boolean                                                                  | Specify true if the script requires elevated privileges to run; otherwise, false.<br/>                                                              |
| RequiresInteractivity | xs:boolean                                                                  | Specify true if the script uses interactions; otherwise, false. If false, you cannot use the [Get-DiagInput](get-diaginput-cmdlet.md) cmdlet.<br/> |



## Remarks

You must specify all children; specifying a subset of the children generates an error.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Script (Resolver) Element**](package-script-resolver-element.md)
</dt> <dt>

[**Script (Troubleshooter) Element**](package-script-troubleshooter-element.md)
</dt> <dt>

[**Script (Verifier) Element**](package-script-verifier-element.md)
</dt> </dl>

 

 





