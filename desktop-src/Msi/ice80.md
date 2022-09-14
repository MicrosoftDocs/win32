---
description: ICE80 validates that the value of the Template Summary Property (PID\_TEMPLATE) correctly specifies &\#0034;Intel64&\#0034;, &\#0034;x64&\#0034;, or &\#0034;Intel&\#0034; depending on the presence of 64-bit components or custom action scripts.
ms.assetid: fd2a15cf-d117-4a87-a26e-caff4b12a2e9
title: ICE80
ms.topic: article
ms.date: 05/31/2018
---

# ICE80

ICE80 validates that the value of the [**Template Summary**](template-summary.md) Property (PID\_TEMPLATE) correctly specifies "Intel64", "x64", "Arm64", or "Intel" depending on the presence of 64-bit components or custom action scripts. ICE80 checks the [Component Table](component-table.md) for any components with the **msidbComponentAttributes64bit** attribute and checks the [CustomAction Table](customaction-table.md) for any scripts with the **msidbCustomActionType64BitScript** attribute. ICE80 verifies that a package with "Intel64", "x64", or "Arm64" in its **Template Summary** Property also has a [**Page Count Summary**](page-count-summary.md) Property (PID\_PAGECOUNT) of at least 150.

ICE80 also validates that the language ID specified by the [**ProductLanguage**](productlanguage.md) property must be contained in the [**Template Summary**](template-summary.md) Property.

For more information, see [Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md).

## Result

ICE80 posts the following errors.



| Error                                                                                                                                                                   | Description                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This package contains 64 bit component '\[1\]' but the [**Template Summary**](template-summary.md) Property does not contain Intel64, x64, or Arm64.                    | The [Component Table](component-table.md)contains a component with the **msidbComponentAttributes64bit** attribute and the [**Template Summary**](template-summary.md) Property does not contain Intel64, x64, or Arm64.        |
| This package contains 64 bit custom action script '\[1\]' but the [**Template Summary**](template-summary.md) Property does not contain Intel64, x64, or Arm64.         | [CustomAction Table](customaction-table.md) contains a script custom action with the **msidbCustomActionType64BitScript** but the [**Template Summary**](template-summary.md) Property does not contain Intel64, x64, or Arm64. |
| Bad value in Summary Information Stream for %s.                                                                                                                         | Returned for PID\_TEMPLATE property if that property is an empty string or not a VT\_LPSTR type. Returned for PID\_PAGECOUNT if that property it is not a VT\_I4 type.<br/>                                         |
| This package is marked with Intel64 but it has a schema less than 150.                                                                                                  | The PID\_TEMPLATE property of the package is Intel64, but its PID\_PAGECOUNT property is less than 150.                                                                                                            |
| This package is marked with x64 but it has a schema less than 200.                                                                                                      | The PID\_TEMPLATE property of the package is x64, but its PID\_PAGECOUNT property is less than 200.                                                                                                            |
| This package is marked with Arm64 but it has a schema less than 500.                                                                                                    | The PID\_TEMPLATE property of the package is Arm64, but its PID\_PAGECOUNT property is less than 500.                                                                                                            |
| This 32Bit Package is using 64 bit property \[1\]                                                                                                                       | A 32-bit package is using a 64-bit property.                                                                                                                                                                              |
| This 32Bit Package is using 64 bit Locator Type in RegLocator table entry \[1\]                                                                                         | A 32-bit package contains **msidbLocatorType64bit** in the Type field of the [RegLocator table](reglocator-table.md).                                                                                                    |
| This 64BitComponent \[1\] uses 32BitDirectory \[3\]                                                                                                                     | A 64-bit component is using a 32-bit directory.                                                                                                                                                                           |
| This 32BitComponent \[1\] uses 64BitDirectory \[3\]                                                                                                                     | A 32-bit component is using a 64-bit directory.                                                                                                                                                                           |
| The '[**ProductLanguage**](productlanguage.md)' property in the Property table has a value of '\[2\]', which is not contained in the Template Summary Property stream. | The value of the [**ProductLanguage**](productlanguage.md) property is not listed in the [**Template Summary**](template-summary.md) property.                                                                          |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> <dt>

[Windows Installer on 64-bit Operating Systems](windows-installer-on-64-bit-operating-systems.md)
</dt> </dl>

 

 




