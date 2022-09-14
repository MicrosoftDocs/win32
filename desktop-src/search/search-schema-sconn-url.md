---
description: The &lt;url&gt; element specifies a URL for the location for this search connector.
ms.assetid: fdc9e138-2e98-4f01-ab7b-0c3dfad5a4dd
title: simpleLocation url Element (Search Connector Schema)
ms.topic: article
ms.date: 05/31/2018
---

# simpleLocation url Element (Search Connector Schema)

The &lt;url&gt; element specifies a URL for the location for this search connector. This value can be a regular file:// URL as defined in the RFC 1738 (https://www.ietf.org/rfc/rfc1738.txt) document or or a URL that uses the knownfolders: protocol. This element has no child elements and no attributes.

## Syntax


```
<!-- url element for simpleLocation -->
    <xs:complexType name="searchConnectorDescriptionType">
        <xs:all>
            ...
            <xs:element name="simpleLocation" type="shellLinkType" minOccurs="0">
                <xs:all>
                    <xs:element name="url" type="xs:anyURI"/>
                    <xs:element name="serialized" minOccurs="0"/>
                </xs:all>
                
            </xs:element>
            ...
        </xs:all>
        <xs:attribute name="publisher" type="xs:string"/>
        <xs:attribute name="product" type="xs:string"/>
    </xs:complexType>
```



## Element Information



| Parent Element                                                                             | Child Elements |
|--------------------------------------------------------------------------------------------|----------------|
| [simpleLocation Element (Search Connector Schema)](search-schema-sconn-simplelocation.md) |                |



 

## Remarks

See [KNOWNFOLDERID](/windows/desktop/shell/knownfolderid) for a list of known folder GUIDs. Use the following format for the value of this element when using the knownfolder: protocol.


```
<url>knownfolder:{ED4824AF-DCE4-45A8-81E2-FC7965083634}</url>
```



The following table shows the Windows 7 known folder GUIDs.



| Known folder                     | GUID                                         |
|----------------------------------|----------------------------------------------|
| FOLDERID\_AdminTools             | {724EF170-A42D-4FEF-9F-26-B6-0E-84-6F-BA-4F} |
| FOLDERID\_AppUpdates             | {a305ce99-f527-492b-8b-1a-7e-76-fa-98-d6-e4} |
| FOLDERID\_AddNewPrograms         | {de61d971-5ebc-4f02-a3-a9-6c-82-89-5e-5c-04} |
| FOLDERID\_CDBurning              | {9E52AB10-F80D-49DF-AC-B8-43-30-F5-68-78-55} |
| FOLDERID\_ChangeRemovePrograms   | {df7266ac-9274-4867-8d-55-3b-d6-61-de-87-2d} |
| FOLDERID\_CommonAdminTools       | {D0384E7D-BAC3-4797-8F-14-CB-A2-29-B3-92-B5} |
| FOLDERID\_CommonOEMLinks         | {C1BAE2D0-10DF-4334-BE-DD-7A-A2-0B-22-7A-9D} |
| FOLDERID\_CommonPrograms         | {0139D44E-6AFE-49F2-86-90-3D-AF-CA-E6-FF-B8} |
| FOLDERID\_CommonStartMenu        | {A4115719-D62E-491D-AA-7C-E7-4B-8B-E3-B0-67} |
| FOLDERID\_CommonStartup          | {82A5EA35-D9CD-47C5-96-29-E1-5D-2F-71-4E-6E} |
| FOLDERID\_CommonTemplates        | {B94237E7-57AC-4347-91-51-B0-8C-6C-32-D1-F7} |
| FOLDERID\_ComputerFolder         | {0AC0837C-BBF8-452A-85-0D-79-D0-8E-66-7C-A7} |
| FOLDERID\_ConflictFolder         | {4bfefb45-347d-4006-a5-be-ac-0c-b0-56-71-92} |
| FOLDERID\_ConnectionsFolder      | {6F0CD92B-2E97-45D1-88-FF-B0-D1-86-B8-DE-DD} |
| FOLDERID\_Contacts               | {56784854-c6cb-462b-81-69-88-e3-50-ac-b8-82} |
| FOLDERID\_ControlPanelFolder     | {82A74AEB-AEB4-465C-A0-14-D0-97-EE-34-6D-63} |
| FOLDERID\_Cookies                | {2B0F765D-C0E9-4171-90-8E-08-A6-11-B8-4F-F6} |
| FOLDERID\_Desktop                | {B4BFCC3A-DB2C-424C-B0-29-7F-E9-9A-87-C6-41} |
| FOLDERID\_DeviceMetadataStore    | {5ce4a5e9-e4eb-479d-b8-9f-13-0c-02-88-61-55} |
| FOLDERID\_Documents              | {FDD39AD0-238F-46AF-AD-B4-6C-85-48-03-69-C7} |
| FOLDERID\_DocumentsLibrary       | {7b0db17d-9cd2-4a93-97-33-46-cc-89-02-2e-7c} |
| FOLDERID\_Downloads              | {374de290-123f-4565-91-64-39-c4-92-5e-46-7b} |
| FOLDERID\_Favorites              | {1777F761-68AD-4D8A-87-BD-30-B7-59-FA-33-DD} |
| FOLDERID\_Fonts                  | {FD228CB7-AE11-4AE3-86-4C-16-F3-91-0A-B8-FE} |
| FOLDERID\_Games                  | {cac52c1a-b53d-4edc-92-d7-6b-2e-8a-c1-94-34} |
| FOLDERID\_GameTasks              | {54fae61-4dd8-4787-80-b6-9-2-20-c4-b7-0}     |
| FOLDERID\_History                | {D9DC8A3B-B784-432E-A7-81-5A-11-30-A7-59-63} |
| FOLDERID\_HomeGroup              | {52528a6b-b9e3-4add-b6-d-58-8c-2d-ba-84-2d}  |
| FOLDERID\_ImplicitAppShortcuts   | {bcb5256f-79f6-4cee-b7-25-dc-34-e4-2-fd-46}  |
| FOLDERID\_InternetCache          | {352481E8-33BE-4251-BA-85-60-07-CA-ED-CF-9D} |
| FOLDERID\_InternetFolder         | {4D9F7874-4E0C-4904-96-7B-40-B0-D2-0C-3E-4B} |
| FOLDERID\_Libraries              | {1b3ea5dc-b587-4786-b4-ef-bd-1d-c3-32-ae-ae} |
| FOLDERID\_Links                  | {bfb9d5e0-c6a9-404c-b2-b2-ae-6d-b6-af-49-68} |
| FOLDERID\_LocalAppData           | {F1B32785-6FBA-4FCF-9D-55-7B-8E-7F-15-70-91} |
| FOLDERID\_LocalAppDataLow        | {A520A1A4-1780-4FF6-BD-18-16-73-43-C5-AF-16} |
| FOLDERID\_LocalizedResourcesDir  | {2A00375E-224C-49DE-B8-D1-44-0D-F7-EF-3D-DC} |
| FOLDERID\_Music                  | {4BD8D571-6D19-48D3-BE-97-42-22-20-08-0E-43} |
| FOLDERID\_MusicLibrary           | {2112ab0a-c86a-4ffe-a3-68-d-e9-6e-47-1-2e}   |
| FOLDERID\_NetHood                | {C5ABBF53-E17F-4121-89-00-86-62-6F-C2-C9-73} |
| FOLDERID\_NetworkFolder          | {D20BEEC4-5CA8-4905-AE-3B-BF-25-1E-A0-9B-53} |
| FOLDERID\_OriginalImages         | {2C36C0AA-5812-4b87-bf-d0-4c-d0-df-b1-9b-39} |
| FOLDERID\_PhotoAlbums            | {69D2CF90-FC33-4FB7-9A-0C-EB-B0-F0-FC-B4-3C} |
| FOLDERID\_Pictures               | {33E28130-4E1E-4676-83-5A-98-39-5C-3B-C3-BB} |
| FOLDERID\_PicturesLibrary        | {a990ae9f-a03b-4e80-94-bc-99-12-d7-50-41-4}  |
| FOLDERID\_Playlists              | {DE92C1C7-837F-4F69-A3-BB-86-E6-31-20-4A-23} |
| FOLDERID\_PrintersFolder         | {76FC4E2D-D6AD-4519-A6-63-37-BD-56-06-81-85} |
| FOLDERID\_PrintHood              | {9274BD8D-CFD1-41C3-B3-5E-B1-3F-55-A7-58-F4} |
| FOLDERID\_Profile                | {5E6C858F-0E22-4760-9A-FE-EA-33-17-B6-71-73} |
| FOLDERID\_ProgramData            | {62AB5D82-FDC1-4DC3-A9-DD-07-0D-1D-49-5D-97} |
| FOLDERID\_ProgramFilesX86        | {7C5A40EF-A0FB-4BFC-87-4A-C0-F2-E0-B9-FA-8E} |
| FOLDERID\_ProgramFilesCommonX86  | {DE974D24-D9C6-4D3E-BF-91-F4-45-51-20-B9-17} |
| FOLDERID\_ProgramFilesX64        | {6d809377-6af0-444b-89-57-a3-77-3f-02-20-0e} |
| FOLDERID\_ProgramFilesCommonX64  | {6365d5a7-f0d-45e5-87-f6-d-a5-6b-6a-4f-7d}   |
| FOLDERID\_ProgramFiles           | {905e63b6-c1bf-494e-b2-9c-65-b7-32-d3-d2-1a} |
| FOLDERID\_ProgramFilesCommon     | {F7F1ED05-9F6D-47A2-AA-AE-29-D3-17-C6-F0-66} |
| FOLDERID\_Programs               | {A77F5D77-2E2B-44C3-A6-A2-AB-A6-01-05-4A-51} |
| FOLDERID\_Public                 | {DFDF76A2-C82A-4D63-90-6A-56-44-AC-45-73-85} |
| FOLDERID\_PublicDesktop          | {C4AA340D-F20F-4863-AF-EF-F8-7E-F2-E6-BA-25} |
| FOLDERID\_PublicDocuments        | {ED4824AF-DCE4-45A8-81-E2-FC-79-65-08-36-34} |
| FOLDERID\_PublicDownloads        | {3d644c9b-1fb8-4f30-9b-45-f6-70-23-5f-79-c0} |
| FOLDERID\_PublicGameTasks        | {debf2536-e1a8-4c59-b6-a2-41-45-86-47-6a-ea} |
| FOLDERID\_PublicMusic            | {3214FAB5-9757-4298-BB-61-92-A9-DE-AA-44-FF} |
| FOLDERID\_PublicPictures         | {B6EBFB86-6907-413C-9A-F7-4F-C2-AB-F0-7C-C5} |
| FOLDERID\_PublicRingtones        | {E555AB60-153B-4D17-9F-04-A5-FE-99-FC-15-EC} |
| FOLDERID\_PublicVideos           | {2400183A-6185-49FB-A2-D8-4A-39-2A-60-2B-A3} |
| FOLDERID\_QuickLaunch            | {52a4f021-7b75-48a9-9f-6b-4b-87-a2-10-bc-8f} |
| FOLDERID\_Recent                 | {AE50C081-EBD2-438A-86-55-8A-09-2E-34-98-7A} |
| FOLDERID\_RecordedTVLibrary      | {1a6fdba2-f42d-4358-a7-98-b7-4d-74-59-26-c5} |
| FOLDERID\_RecycleBinFolder       | {B7534046-3ECB-4C18-BE-4E-64-CD-4C-B7-D6-AC} |
| FOLDERID\_ResourceDir            | {8AD10C31-2ADB-4296-A8-F7-E4-70-12-32-C9-72} |
| FOLDERID\_Ringtones              | {C870044B-F49E-4126-A9-C3-B5-2A-1F-F4-11-E8} |
| FOLDERID\_RoamingAppData         | {3EB685DB-65F9-4CF6-A0-3A-E3-EF-65-72-9F-3D} |
| FOLDERID\_SamplePlaylists        | {15CA69B3-30EE-49C1-AC-E1-6B-5E-C3-72-AF-B5} |
| FOLDERID\_SampleMusic            | {B250C668-F57D-4EE1-A6-3C-29-0E-E7-D1-AA-1F} |
| FOLDERID\_SamplePictures         | {C4900540-2379-4C75-84-4B-64-E6-FA-F8-71-6B} |
| FOLDERID\_SampleVideos           | {859EAD94-2E85-48AD-A7-1A-09-69-CB-56-A6-CD} |
| FOLDERID\_SavedGames             | {4c5c32ff-bb9d-43b0-b5-b4-2d-72-e5-4e-aa-a4} |
| FOLDERID\_SavedSearches          | {7d1d3a04-debb-4115-95-cf-2f-29-da-29-20-da} |
| FOLDERID\_SEARCH\_CSC            | {ee32e446-31ca-4aba-81-4f-a5-eb-d2-fd-6d-5e} |
| FOLDERID\_SEARCH\_MAPI           | {98ec0e18-2098-4d44-86-44-66-97-93-15-a2-81} |
| FOLDERID\_SearchHome             | {190337d1-b8ca-4121-a6-39-6d-47-2d-16-97-2a} |
| FOLDERID\_SendTo                 | {8983036C-27C0-404B-8F-08-10-2D-10-DC-FD-74} |
| FOLDERID\_StartMenu              | {625B53C3-AB48-4EC1-BA-1F-A1-EF-41-46-FC-19} |
| FOLDERID\_Startup                | {B97D20BB-F46A-4C97-BA-10-5E-36-08-43-08-54} |
| FOLDERID\_SyncManagerFolder      | {43668BF8-C14E-49B2-97-C9-74-77-84-D7-84-B7} |
| FOLDERID\_SyncResultsFolder      | {289a9a43-be44-4057-a4-1b-58-7a-76-d7-e7-f9} |
| FOLDERID\_SyncSetupFolder        | {f214138-b1d3-4a90-bb-a9-27-cb-c0-c5-38-9a}  |
| FOLDERID\_System                 | {1AC14E77-02E7-4E5D-B7-44-2E-B1-AE-51-98-B7} |
| FOLDERID\_SystemX86              | {D65231B0-B2F1-4857-A4-CE-A8-E7-C6-EA-7D-27} |
| FOLDERID\_Templates              | {A63293E8-664E-48DB-A0-79-DF-75-9E-05-09-F7} |
| FOLDERID\_UserPinned             | {9e3995ab-1f9c-4f13-b8-27-48-b2-4b-6c-71-74} |
| FOLDERID\_UsersFiles             | {f3ce0f7c-4901-4acc-86-48-d5-d4-4b-04-ef-8f} |
| FOLDERID\_UsersLibraries         | {a302545d-deff-464b-ab-e8-61-c8-64-8d-93-9b} |
| FOLDERID\_UserProfiles           | {0762D272-C50A-4BB0-A3-82-69-7D-CD-72-9B-80} |
| FOLDERID\_UserProgramFiles       | {5cd7aee2-2219-4a67-b8-5d-6c-9c-e1-56-60-cb} |
| FOLDERID\_UserProgramFilesCommon | {bcbd3057-ca5c-4622-b4-2d-bc-56-db-0a-e5-16} |
| FOLDERID\_Videos                 | {18989B1D-99B5-455B-84-1C-AB-7C-74-E4-DD-FC} |
| FOLDERID\_VideosLibrary {        | 491e922f-5643-4af4-a7-eb-4e-7a-13-8d-81-74}  |
| FOLDERID\_Windows {              | F38BF404-1D43-42F2-93-05-67-DE-0B-28-FC-23}  |



 

## Examples


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <simpleLocation>
        <url>mapi://{S-1-5-21-2127521184-1604012920-1887927527-2779359}/</url>
    </simpleLocation>
    ...
</searchConnectionDescription>
```




```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    ...
    <simpleLocation>
        <url>knownfolder:{ED4824AF-DCE4-45A8-81E2-FC7965083634}</url>
    </simpleLocation>
    ...
</searchConnectionDescription>
```



## Related topics

<dl> <dt>

[KNOWNFOLDERID](/windows/desktop/shell/knownfolderid)
</dt> </dl>

 

 
