---
description: How to access System Management BIOS (SMBIOS) information from a Universal Windows app.
ms.assetid: 4D185319-C093-4B1B-A182-E845E72FEA5D
title: Access SMBIOS information from a Universal Windows App
ms.topic: article
ms.date: 05/31/2018
---

# Access SMBIOS information from a Universal Windows App

> [NOTE]
> Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

How to access System Management BIOS (SMBIOS) information from a Universal Windows app.

## Access SMBIOS information from a Universal Windows Platform App

Starting with Windows 10, version 1803, Universal Windows apps can use [GetSystemFirmwareTable](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable) and [EnumSystemFirmwareTables](/windows/win32/api/sysinfoapi/nf-sysinfoapi-enumsystemfirmwaretables) to access SMBIOS information by declaring the **smbios** restricted capability in the app manifest.

> [!IMPORTANT]
> Only access to raw SMBIOS (RSMB) firmware tables is supported from a Universal Windows app. **ACCESS\_DENIED** will be returned if you try to access other firmware table types from a Universal Windows app.

 

To declare the **smbios** restricted capability in the app manifest, add the **rescap** namespace and **smbios** capability as follows:

``` syntax
<Package
  ...
  xmlns:rescap="http://schemas.microsoft.com/appx/manifest/foundation/windows10/restrictedcapabilities"
  IgnorableNamespaces="uap mp rescap">  
  ...
  <Capabilities>
    <rescap:Capability Name="smbios"/>
  </Capabilities>
</Package>
```

## Related topics

<dl> <dt>

[Restricted capabilities](/windows/uwp/packaging/app-capability-declarations#restricted-capabilities)
</dt> <dt>

[GetSystemFirmwareTable](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable)
</dt> <dt>

[EnumSystemFirmwareTables](/windows/win32/api/sysinfoapi/nf-sysinfoapi-enumsystemfirmwaretables)
</dt> <dt>

[Access UEFI firmware variables from a Universal Windows App](access-uefi-firmware-variables-from-a-universal-windows-app.md)
</dt> </dl>

 

 
