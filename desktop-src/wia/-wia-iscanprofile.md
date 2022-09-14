---
description: The IScanProfile interface represents a single scan profile and enables applications to set and get the properties of the profile.
ms.assetid: 5cd76256-d64e-4934-8cc2-0a467c7e34a9
title: IScanProfile interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IScanProfile
api_type: 
- COM
api_location: 
- Scanprofiles.idl
---

# IScanProfile interface

The **IScanProfile** interface represents a single scan profile and enables applications to set and get the properties of the profile.

## Members

The **IScanProfile** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IScanProfile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IScanProfile** interface has these methods.



| Method                                                     | Description                                                                                                                                         |
|:-----------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAllPropIDs**](-wia-iscanprofile-getallpropids.md)   | Gets all available property IDs in a profile.<br/>                                                                                            |
| [**GetDeviceID**](-wia-iscanprofile-getdeviceid.md)       | Returns the ID of the device.<br/>                                                                                                            |
| [**GetGUID**](-wia-iscanprofile-getguid.md)               | Returns the GUID of the profile.<br/>                                                                                                         |
| [**GetItem**](-wia-iscanprofile-getitem.md)               | Gets the GUID of the category of the WIA 2.0 item that the profile is associated with.<br/>                                                   |
| [**GetName**](-wia-iscanprofile-getname.md)               | Gets the friendly name of the profile.<br/>                                                                                                   |
| [**GetNumPropIDS**](-wia-iscanprofile-getnumpropids.md)   | Gets the number of property IDs in a profile.<br/>                                                                                            |
| [**GetProperty**](-wia-iscanprofile-getproperty.md)       | Gets the value of specified child properties in the `<Properties>` element of a scan profile.<br/>                                            |
| [**IsDefault**](-wia-iscanprofile-isdefault.md)           | Gets a value that indicates whether the profile is the default scan profile of an associated [**IWiaItem2**](-wia-iwiaitem2.md) device.<br/> |
| [**RemoveProperty**](-wia-iscanprofile-removeproperty.md) | Removes a specified list of child properties in the `<Properties>` element of a scan profile.<br/>                                            |
| [**Save**](-wia-iscanprofile-save.md)                     | Saves changes to a profile to disk.<br/>                                                                                                      |
| [**SetItem**](-wia-iscanprofile-setitem.md)               | Sets the GUID of the category of WIA 2.0 item that the profile is associated with.<br/>                                                       |
| [**SetName**](-wia-iscanprofile-setname.md)               | Sets the friendly name of the profile.<br/>                                                                                                   |
| [**SetProperty**](-wia-iscanprofile-setproperty.md)       | Sets the value of specified child properties in the `<Properties>` element of a scan profile.<br/>                                            |



 

## Remarks

Any [**IWiaItem2**](-wia-iwiaitem2.md) device can have a scan profile. However, **IWiaItem2** items of types WIA\_CATEGORY\_FINISHED\_FILE and WIA\_CATEGORY\_ROOT cannot have profiles.

If a scan profile is saved using the [**IScanProfile::Save**](-wia-iscanprofile-save.md) method, it is stored as an XML file at %USERPROFILE%\\Application Data\\Microsoft\\Document Center\\UserScanProfiles.

To create an instance of an **IScanProfile** object, use the [**IScanProfileMgr::CreateProfile**](-wia-iscanprofilemgr-createprofile.md) method. To get a reference to a scan profile that has already been saved to disk, use the [**IScanProfileMgr::OpenProfile**](-wia-iscanprofilemgr-openprofile.md) method.

All scan profiles have the following elements: `<ProfileGUID>, <DeviceID>, <ProfileName>, <WiaItem>`, and `<Properties>`. The default profile of a device also has a `<Default>` element.

The `<ProfileGUID>` and `<DeviceID>` elements cannot be changed after the profile is created. The values of the `<ProfileName>` element and the `<WiaItem>` element can be changed after the profile is created. The `<Default>` element can be added or deleted. This can be done programatically with the [**IScanProfile::SetName**](-wia-iscanprofile-setname.md), [**IScanProfile::SetItem**](-wia-iscanprofile-setitem.md), and [**IScanProfileMgr::SetDefault**](-wia-iscanprofilemgr-setdefault.md) methods. These properties can also be changed by users through the [**IScanProfileUI::ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) method.

The `<Properties>` element contains `<Property>` children. Use these to add any WIA 2.0 item or device property to the profile. You can also develop your own image acquistion `<Property>` children. This makes the Scan Profile Schema extensible. (For more information about extending the schema, see [Defining Custom Properties](-wia-defining-custom-properties.md), [**IScanProfile::GetProperty**](-wia-iscanprofile-getproperty.md), and [**IScanProfile::SetProperty**](-wia-iscanprofile-setproperty.md).)

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                        |
| IDL<br/>                      | <dl> <dt>Scanprofiles.idl</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> <dt>

[Scan Profile Schema](-wia-scan-profile-schema.md)
</dt> </dl>

 

 
