---
description: Wmiadap is a application that runs on Windows that can update performance information in the WMI repository.
ms.assetid: 459fe19e-3e2e-4a58-b3e7-75fd285f7389
ms.tgt_platform: multiple
title: wmiadap
ms.topic: article
ms.date: 05/31/2018
---

# wmiadap

Wmiadap is a application that runs on Windows that can update performance information in the WMI repository. Generally, this allows developers and IT Administrators to create scripts that access performance information, such as the amount of memory used by an application. The following topic describes the command-line interface you can use to control how wmiadap retrieves information.

Wmiadap is installed with the operating system on most systems, in the C:\\Windows\\System32\\wbem directory. If you are seeing error messages concerning wmiadap.exe, search [Microsoft Support](https://support.microsoft.com/). Generally, you should not delete wmiadap.exe from your system, unless otherwise instructed.

The transfer of data from the performance libraries and the refresh of classes derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) is done by the [WmiPerfClass](wmi-providers.md) and [WMIPerfInst](wmi-providers.md) providers. The WmiPerfClass provider updates WMI [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes) only when a new performance object is added. You still can run Wmiadap with the **/r** switch to parse the Windows Driver Model drivers to create performance objects. The **/f** switch still forces an update of the WMI classes from the performance libraries.

The following switches are available at the command prompt.

**wmiadap** \[**/f**\]\[**/r**\]

## Switches

<dl> <dt>

<span id="_f"></span><span id="_F"></span>**/f**
</dt> <dd>

Parses all the performance libraries on the system and refreshes the classes derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata).

</dd> <dt>

<span id="_r"></span><span id="_R"></span>**/r**
</dt> <dd>

Parses all the Windows Driver Model drivers on the system to create performance objects.

</dd> </dl>

## See also

<dl> <dt>

[Performance Libraries and WMI](performance-libraries-and-wmi.md)
</dt> <dt>

[**winmgmt**](winmgmt.md)
</dt> </dl>

 

 
