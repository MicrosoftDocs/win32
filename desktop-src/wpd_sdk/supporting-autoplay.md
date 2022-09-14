---
description: Supporting AutoPlay
ms.assetid: e91334d9-9041-4cb8-a6d0-0e2371800064
title: Supporting AutoPlay
ms.topic: article
ms.date: 05/31/2018
---

# Supporting AutoPlay

AutoPlay is a feature of the Shell that launches applications associated with particular devices. Depending on the current AutoPlay settings, this feature will perform one of several actions, such as presenting a list of available handler applications, displaying a standard folder view of files, and so on.

In Windows Vista, the AutoPlay feature was extended so that a WPD device can provide a list of content types that it supports. Similarly, WPD applications can register content types that they support. For example, a photo acquisition wizard can register as a handler for any WPD device that provides images, and a multimedia application can register as a handler for any device that stores audio or video files.

Applications register handler-specific information by writing entries to the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers\\Handlers** key. Using a WPD application handler (named MyWpdApplication.exe) as an example, the application may insert the following values under a **\\Handlers\\MyWpdApplicationHandler** key.



| Value          | Type            | Data                                                 |
|----------------|-----------------|------------------------------------------------------|
| Action         | REG\_SZ         | Browse content on portable devices.                  |
| CLSIDForCancel | REG\_SZ         | {00000000-0000-0000-0000-000000000000}               |
| DefaultIcon    | REG\_EXPAND\_SZ | %SystemDrive%\\multimedia\\wpd\\MyWpdApplication.exe |
| InitCmdLine    | REG\_SZ         | /AutoPlay                                            |
| ProgID         | REG\_SZ         | MyWpdApplication.MyWpdApplicationAutoPlay            |
| Provider       | REG\_SZ         | MyWpdApplication                                     |



 

For more information about the AutoPlay registry keys and values found under the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers\\Handlers** key, see the corresponding documentation on MSDN.

### The WPD AutoPlay Scheme

The WPD AutoPlay scheme integrates with the Windows Vista AutoPlay feature. It does so by supporting three AutoPlay categories, which are described in the following table.



| Category | Description                                                                                                          |
|----------|----------------------------------------------------------------------------------------------------------------------|
| Source   | A WPD device can be treated as a source of content (that is, the content can be transferred from the device).        |
| Sink     | A WPD device can be treated as a destination for content (that is, the content can be transferred to the device).    |
| Function | A WPD device supports a programmable or controllable capability (for example, it can send and receive SMS messages). |



 

Applications register for the appropriate source, sink, and/or function category by writing entries to the AutoPlay section of the system registry. These entries appear under the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers\\EventHandlers\\WPD** key. Under the WPD key are the **Function**, **Sink**, and **Source** keys. Under each of these keys is a GUID that corresponds to a WPD functional category or content type.

The following table lists the GUIDs found under the **Function** key in the registry and identifies the functional category that corresponds to each GUID.



| WPD Functional Category                           | Registry Key (GUID)                    |
|---------------------------------------------------|----------------------------------------|
| WPD\_FUNCTIONAL\_CATEGORY\_ALL                    | {2D8A6512-A74C-448E-BA8A-F4AC07C49399} |
| WPD\_FUNCTIONAL\_CATEGORY\_AUDIO\_CAPTURE         | {3F2A1919-C7C2-4A00-855D-F57CF06DEBBB} |
| WPD\_FUNCTIONAL\_CATEGORY\_DEVICE                 | {08EA466B-E3A4-4336-A1F3-A44D2B5C438C} |
| WPD\_FUNCTIONAL\_CATEGORY\_NETWORK\_CONFIGURATION | {48F4DB72-7C6A-4AB0-9E1A-470E3CDBF26A} |
| WPD\_FUNCTIONAL\_CATEGORY\_RENDERING\_INFORMATION | {08600BA4-A7BA-4A01-AB0E-0065D0A356D3} |
| WPD\_FUNCTIONAL\_CATEGORY\_SMS                    | {0044A0B1-C1E9-4AFD-B358-A62C6117C9CF} |
| WPD\_FUNCTIONAL\_CATEGORY\_STILL\_IMAGE\_CAPTURE  | {613CA327-AB93-4900-B4FA-895BB5874B79} |
| WPD\_FUNCTIONAL\_CATEGORY\_STORAGE                | {23F05BBC-15DE-4C2A-A55B-A9AF5CE412EF} |
| WPD\_FUNCTIONAL\_CATEGORY\_VIDEO\_CAPTURE         | {E23E5F6B-7243-43AA-8DF1-0EB3D968A918} |



 

The following table lists the GUIDS found under the **Sink** and the **Source** keys in the registry and identifies the content type that corresponds to each GUID.



| WPD Content Type                          | Registry Key (GUID)                    |
|-------------------------------------------|----------------------------------------|
| WPD\_CONTENT\_TYPE\_ALL                   | {80E170D2-1055-4A3E-B952-82CC4F8A8689} |
| WPD\_CONTENT\_TYPE\_APPOINTMENT           | {0FED060E-8793-4B1E-90C9-48AC389AC631} |
| WPD\_CONTENT\_TYPE\_AUDIO                 | {4AD2C85E-5E2D-45E5-8864-4F229E3C6CF0} |
| WPD\_CONTENT\_TYPE\_AUDIO\_ALBUM          | {AA18737E-5009-48FA-AE21-85F24383B4E6} |
| WPD\_CONTENT\_TYPE\_CALENDAR              | {A1FD5967-6023-49A0-9DF1-F8060BE751B0} |
| WPD\_CONTENT\_TYPE\_CERTIFICATE           | {DC3876E8-A948-4060-9050-CBD77E8A3D87} |
| WPD\_CONTENT\_TYPE\_CONTACT               | {EABA8313-4525-4707-9F0E-87C6808E9435} |
| WPD\_CONTENT\_TYPE\_CONTACT\_GROUP        | {346B8932-4C36-40D8-9415-1828291F9DE9} |
| WPD\_CONTENT\_TYPE\_DOCUMENT              | {680ADF52-950A-4041-9B41-65E393648155} |
| WPD\_CONTENT\_TYPE\_EMAIL                 | {8038044A-7E51-4F8F-883D-1D0623D14533} |
| WPD\_CONTENT\_TYPE\_FOLDER                | {27E2E392-A111-48E0-AB0C-E17705A05F85} |
| WPD\_CONTENT\_TYPE\_FUNCTIONAL\_OBJECT    | {99ED0160-17FF-4C44-9D98-1D7A6F941921} |
| WPD\_CONTENT\_TYPE\_GENERIC\_FILE         | {0085E0A6-8D34-45D7-BC5C-447E59C73D48} |
| WPD\_CONTENT\_TYPE\_GENERIC\_MESSAGE      | {E80EAAF8-B2DB-4133-B67E-1BEF4B4A6E5F} |
| WPD\_CONTENT\_TYPE\_IMAGE                 | {EF2107D5-A52A-4243-A26B-62D4176D7603} |
| WPD\_CONTENT\_TYPE\_IMAGE\_ALBUM          | {75793148-15F5-4A30-A813-54ED8A37E226} |
| WPD\_CONTENT\_TYPE\_MEDIA\_CAST           | {5E88B3CC-3E65-4E62-BFFF-229495253AB0} |
| WPD\_CONTENT\_TYPE\_MEMO                  | {9CD20ECF-3B50-414F-A641-E473FFE45751} |
| WPD\_CONTENT\_TYPE\_MIXED\_CONTENT\_ALBUM | {00F0C3AC-A593-49AC-9219-24ABCA5A2563} |
| WPD\_CONTENT\_TYPE\_NETWORK\_ASSOCIATION  | {031DA7EE-18C8-4205-847E-89A11261D0F3} |
| WPD\_CONTENT\_TYPE\_PLAYLIST              | {1A33F7E4-AF13-48F5-994E-77369DFE04A3} |
| WPD\_CONTENT\_TYPE\_PROGRAM               | {D269F96A-247C-4BFF-98FB-97F3C49220E6} |
| WPD\_CONTENT\_TYPE\_SECTION               | {821089F5-1D91-4DC9-BE3C-BBB1B35B18CE} |
| WPD\_CONTENT\_TYPE\_TASK                  | {63252F2C-887F-4CB6-B1AC-D29855DCEF6C} |
| WPD\_CONTENT\_TYPE\_TELEVISION            | {60A169CF-F2AE-4E21-9375-9677F11C1C6E} |
| WPD\_CONTENT\_TYPE\_UNSPECIFIED           | {28D8D31E-249C-454E-AABC-34883168E634} |
| WPD\_CONTENT\_TYPE\_VIDEO                 | {9261B03C-3D78-4519-85E3-02C5E1F50BB9} |
| WPD\_CONTENT\_TYPE\_VIDEO\_ALBUM          | {012B0DB7-D4C1-45D6-B081-94B87779614F} |
| WPD\_CONTENT\_TYPE\_WIRELESS\_PROFILE     | {0BAC070A-9F5F-4DA4-A8F6-3DE44D68FD6C} |



 

If an application supported a particular function, source, or sink category, it would insert a string specifying the name of the handler key under the GUID that identified the supported functional or content-type category. Using MyWpdApplication as an example, the application would create an entry under the …**/EventHandlers/WPD/Function**, or **/Sink**, or **/Source** keys. This entry would have the form "MyWpdApplicationHandler" and be of type REG\_SZ. Also, this entry would appear under the GUID for the functional categories or content types that the application supports.

 

 



