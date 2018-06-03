---
title: DisplayInformation Complex Type
description: Specifies the localized name and description strings that are used for display in a UI component.
ms.assetid: 725e860b-243f-4f35-a234-7d4d9a97acf5
keywords:
- DisplayInformation complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- DisplayInformation
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DisplayInformation Complex Type

Specifies the localized name and description strings that are used for display in a UI component.

``` syntax
<xs:complexType name="DisplayInformation">
    <xs:sequence>
        <xs:element name="Parameters"
            type="dcmPS:Parameters"
            minOccurs="1"
            maxOccurs="1"
        >
            <xs:unique name="No_display_parameters_may_have_the_same_name">
                <xs:selector
                    xpath="Parameter"
                 />
                <xs:field
                    xpath="Name"
                 />
            </xs:unique>
        </xs:element>
        <xs:element name="Name"
            type="dcmRS:MandatoryResource"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Description"
            type="dcmRS:OptionalResource"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element     | Type                                                                     | Description                                                                                                                                                                                                                                                                                          |
|-------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description | [**dcmRS:OptionalResource**](resource-optionalresource-simpletype.md)   | A description of the UI component. The description is optional.<br/>                                                                                                                                                                                                                           |
| Name        | [**dcmRS:MandatoryResource**](resource-mandatoryresource-simpletype.md) | The display name to use for the UI component.<br/>                                                                                                                                                                                                                                             |
| Parameters  | [**dcmPS:Parameters**](package-parameters-complextype.md)               | A list of parameter names. The names must match the parameter names specified in the substitution strings found in Name and Description. For example, if Name contained the string, "The %device% device is %status%.", then the list of parameters should contain "device" and "status".<br/> |



## Remarks

How the strings are used depends on where this node is located in the manifest. For example, if this node is a child of [**LocalDiagnosticPackage**](package-localdiagnosticpackage-complextype.md), the Name and Description provide the name and description of the troubleshooting pack. For single response lists, the Name is used as the display name for a choice in the list and the Description is used as a tooltip when the user hovers the mouse over the choice.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DisplayInformation (Choice) Element**](package-displayinformation-choice-element.md)
</dt> <dt>

[**DisplayInformation (GlobalDiagnosticPackage) Element**](package-displayinformation-globaldiagnosticpackage-element.md)
</dt> <dt>

[**DisplayInformation (GlobalRootcause) Element**](package-displayinformation-globalrootcause-element.md)
</dt> <dt>

[**DisplayInformation (LaunchUIInteraction) Element**](package-displayinformation-launchuiinteraction-element.md)
</dt> <dt>

[**DisplayInformation (MultipleResponseInteraction) Element**](package-displayinformation-multipleresponseinteraction-element.md)
</dt> <dt>

[**DisplayInformation (PauseInteraction) Element**](package-displayinformation-pauseinteraction-element.md)
</dt> <dt>

[**DisplayInformation (SingleResponseInteraction) Element**](package-displayinformation-singleresponseinteraction-element.md)
</dt> <dt>

[**DisplayInformation (TextInteraction) Element**](package-displayinformation-textinteraction-element.md)
</dt> <dt>

[**DisplayInformation (LocalDiagnosticPackage) Element**](package-displayinformation-localdiagnosticpackage-element.md)
</dt> <dt>

[**DisplayInformation (LocalRootcause) Element**](package-displayinformation-localrootcause-element.md)
</dt> <dt>

[**DisplayInformation (Resolver) Element**](package-displayinformation-resolver-element.md)
</dt> </dl>

 

 





