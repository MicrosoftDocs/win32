---
title: Names for WPD GUIDs
description: The following table lists the names that WPD Automation assigns to WPD GUIDs.
ms.assetid: 5050a11e-a642-452c-8b5b-e4609ac7a241
keywords:
- WPD Automation,WPD GUIDs
- WPD Automation,names for WPD GUIDs
- Windows Portable Devices (WPD),WPD Automation
- WPD (Windows Portable Devices),WPD Automation
- Windows Portable Devices (WPD),GUIDs
- WPD (Windows Portable Devices),GUIDs
- Windows Portable Devices (WPD),names for WPD GUIDs
- WPD (Windows Portable Devices),names for WPD GUIDs
- WPD GUIDs,list of
- GUIDs,list of
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Names for WPD GUIDs

The following table lists the names that WPD Automation assigns to WPD GUIDs. The definitions of these GUIDs can be found in the [**WPD Application Programming Interface Programming Reference**](https://msdn.microsoft.com/library/windows/desktop/dd375709). WPD GUIDs are accessed by their WPD Automation names. For example, the WPD Automation Name "**Mp3**" can be used as a parameter in the [**Storage.GetChildrenByFormat**](storage-getchildrenbyformat.md) method, like this:

`storageObject.GetChildrenByFormat("Mp3");`

This will return all immediate **Mp3** child objects where the **WPD\_OBJECT\_FORMAT** is the **WPD\_OBJECT\_FORMAT\_MP3** for each child object.



| WPD GUID                                          | WPD Automation Name       |
|---------------------------------------------------|---------------------------|
| WPD\_EVENT\_OBJECT\_ADDED                         | ObjectAdded               |
| WPD\_EVENT\_OBJECT\_REMOVED                       | ObjectRemoved             |
| WPD\_EVENT\_OBJECT\_UPDATED                       | ObjectUpdated             |
| WPD\_EVENT\_DEVICE\_RESET                         | DeviceReset               |
| WPD\_EVENT\_DEVICE\_CAPABILITIES\_UPDATED         | DeviceCapabilitiesUpdated |
| WPD\_EVENT\_STORAGE\_FORMAT                       | StorageFormat             |
| WPD\_EVENT\_OBJECT\_TRANSFER\_REQUESTED           | ObjectTransferRequested   |
| WPD\_EVENT\_DEVICE\_REMOVED                       | DeviceRemoved             |
| WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT            | FunctionalObject          |
| WPD\_CONTENT\_TYPE\_FOLDER                        | Folder                    |
| WPD\_CONTENT\_TYPE\_IMAGE                         | Image                     |
| WPD\_CONTENT\_TYPE\_DOCUMENT                      | Document                  |
| WPD\_CONTENT\_TYPE\_CONTACT                       | Contact                   |
| WPD\_CONTENT\_TYPE\_CONTACT\_GROUP                | ContactGroup              |
| WPD\_CONTENT\_TYPE\_AUDIO                         | Audio                     |
| WPD\_CONTENT\_TYPE\_VIDEO                         | Video                     |
| WPD\_CONTENT\_TYPE\_TELEVISION                    | Television                |
| WPD\_CONTENT\_TYPE\_PLAYLIST                      | Playlist                  |
| WPD\_CONTENT\_TYPE\_MIXED\_CONTENT\_ALBUM         | MixedContentAlbum         |
| WPD\_CONTENT\_TYPE\_AUDIO\_ALBUM                  | AudioAlbum                |
| WPD\_CONTENT\_TYPE\_IMAGE\_ALBUM                  | ImageAlbum                |
| WPD\_CONTENT\_TYPE\_VIDEO\_ALBUM                  | VideoAlbum                |
| WPD\_CONTENT\_TYPE\_MEMO                          | Memo                      |
| WPD\_CONTENT\_TYPE\_EMAIL                         | Email                     |
| WPD\_CONTENT\_TYPE\_APPOINTMENT                   | Appointment               |
| WPD\_CONTENT\_TYPE\_TASK                          | Task                      |
| WPD\_CONTENT\_TYPE\_PROGRAM                       | Program                   |
| WPD\_CONTENT\_TYPE\_GENERIC\_FILE                 | GenericFile               |
| WPD\_CONTENT\_TYPE\_CALENDAR                      | Calendar                  |
| WPD\_CONTENT\_TYPE\_GENERIC\_MESSAGE              | GenericMessage            |
| WPD\_CONTENT\_TYPE\_NETWORK\_ASSOCIATION          | NetworkAssociation        |
| WPD\_CONTENT\_TYPE\_CERTIFICATE                   | Certificate               |
| WPD\_CONTENT\_TYPE\_WIRELESS\_PROFILE             | WirelessProfile           |
| WPD\_CONTENT\_TYPE\_MEDIA\_CAST                   | MediaCast                 |
| WPD\_CONTENT\_TYPE\_SECTION                       | Section                   |
| WPD\_CONTENT\_TYPE\_UNSPECIFIED                   | UnspecifiedContentType    |
| WPD\_FUNCTIONAL\_CATEGORY\_DEVICE                 | Device                    |
| WPD\_FUNCTIONAL\_CATEGORY\_STORAGE                | Storage                   |
| WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE  | StillImageCapture         |
| WPD\_FUNCTIONAL\_CATEGORY\_AUDIO\_CAPTURE         | AudioCapture              |
| WPD\_FUNCTIONAL\_CATEGORY\_VIDEO\_CAPTURE         | VideoCapture              |
| WPD\_FUNCTIONAL\_CATEGORY\_SMS                    | Sms                       |
| WPD\_FUNCTIONAL\_CATEGORY\_RENDERING\_INFORMATION | RenderingInformation      |
| WPD\_FUNCTIONAL\_CATEGORY\_NETWORK\_CONFIGURATION | NetworkConfiguration      |
| WPD\_OBJECT\_FORMAT\_PROPERTIES\_ONLY             | PropertiesOnly            |
| WPD\_OBJECT\_FORMAT\_UNSPECIFIED                  | UnspecifiedFormat         |
| WPD\_OBJECT\_FORMAT\_SCRIPT                       | Script                    |
| WPD\_OBJECT\_FORMAT\_EXECUTABLE                   | Executable                |
| WPD\_OBJECT\_FORMAT\_TEXT                         | Text                      |
| WPD\_OBJECT\_FORMAT\_HTML                         | Html                      |
| WPD\_OBJECT\_FORMAT\_DPOF                         | Dpof                      |
| WPD\_OBJECT\_FORMAT\_AIFF                         | Aiff                      |
| WPD\_OBJECT\_FORMAT\_WAVE                         | Wave                      |
| WPD\_OBJECT\_FORMAT\_MP3                          | Mp3                       |
| WPD\_OBJECT\_FORMAT\_AVI                          | Avi                       |
| WPD\_OBJECT\_FORMAT\_MPEG                         | Mpeg                      |
| WPD\_OBJECT\_FORMAT\_ASF                          | Asf                       |
| WPD\_OBJECT\_FORMAT\_EXIF                         | Exif                      |
| WPD\_OBJECT\_FORMAT\_TIFFEP                       | Tiffep                    |
| WPD\_OBJECT\_FORMAT\_FLASHPIX                     | Flashpix                  |
| WPD\_OBJECT\_FORMAT\_BMP                          | Bmp                       |
| WPD\_OBJECT\_FORMAT\_CIFF                         | Ciff                      |
| WPD\_OBJECT\_FORMAT\_GIF                          | Gif                       |
| WPD\_OBJECT\_FORMAT\_JFI                          | Jfi                       |
| WPD\_OBJECT\_FORMAT\_PCD                          | Pcd                       |
| WPD\_OBJECT\_FORMAT\_PICT                         | Pict                      |
| WPD\_OBJECT\_FORMAT\_PNG                          | Png                       |
| WPD\_OBJECT\_FORMAT\_TIFF                         | Tiff                      |
| WPD\_OBJECT\_FORMAT\_TIFFIT                       | Tiffit                    |
| WPD\_OBJECT\_FORMAT\_JP2                          | Jp2                       |
| WPD\_OBJECT\_FORMAT\_JPX                          | Jpx                       |
| WPD\_OBJECT\_FORMAT\_WINDOWSIMAGEFORMAT           | WindowsImageFormat        |
| WPD\_OBJECT\_FORMAT\_WMA                          | Wma                       |
| WPD\_OBJECT\_FORMAT\_WMV                          | Wmv                       |
| WPD\_OBJECT\_FORMAT\_WPLPLAYLIST                  | WplPlaylist               |
| WPD\_OBJECT\_FORMAT\_M3UPLAYLIST                  | M3uPlaylist               |
| WPD\_OBJECT\_FORMAT\_MPLPLAYLIST                  | MplPlaylist               |
| WPD\_OBJECT\_FORMAT\_ASXPLAYLIST                  | AsxPlaylist               |
| WPD\_OBJECT\_FORMAT\_PLSPLAYLIST                  | PlsPlaylist               |
| WPD\_OBJECT\_FORMAT\_ABSTRACT\_CONTACT\_GROUP     | AbstractContactGroup      |
| WPD\_OBJECT\_FORMAT\_ABSTRACT\_MEDIA\_CAST        | AbstractMediaCast         |
| WPD\_OBJECT\_FORMAT\_VCALENDAR1                   | Vcalendar1                |
| WPD\_OBJECT\_FORMAT\_ICALENDAR                    | Icalendar                 |
| WPD\_OBJECT\_FORMAT\_ABSTRACT\_CONTACT            | AbstractContact           |
| WPD\_OBJECT\_FORMAT\_VCARD2                       | Vcard                     |
| WPD\_OBJECT\_FORMAT\_VCARD3                       | Vcard3                    |



 

## Related topics

<dl> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> </dl>

 

 




