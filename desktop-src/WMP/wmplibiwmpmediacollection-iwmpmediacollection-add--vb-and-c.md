---
title: IWMPMediaCollection add method
description: The add method adds a new media item or playlist to the library. | IWMPMediaCollection add method
ms.assetid: a3539646-797b-4481-a31e-86771f3633a9
keywords:
- add method Windows Media Player
- add method Windows Media Player , IWMPMediaCollection interface
- IWMPMediaCollection interface Windows Media Player , add method
topic_type:
- apiref
api_name:
- IWMPMediaCollection.add
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPMediaCollection::add method

The **add** method adds a new media item or playlist to the library.

## Syntax


```CSharp
public IWMPMedia add(
  System.String bstrURL
);
```


```VB

Public Function add( _
  ByVal bstrURL As System.String _
) As IWMPMedia
Implements IWMPMediaCollection.add
```





## Parameters

<dl> <dt>

*bstrURL* \[in\]
</dt> <dd>

A **System.String** that is the URL that specifies the location of the media item or playlist.

</dd> </dl>

## Return value

The **WMPLib.IWMPMedia** interface for the added item or playlist.

## Remarks

This method loads an existing media item or playlist into the library, given a path. This method does not move or change the file. This method fails if given an invalid local path, but media items themselves are not checked for validity before they are added to the library.

This method accepts both static and auto playlist files. The **IWMPPlaylistCollection.importPlaylist** method can also be used to add a static playlist to the library.

Before calling this method, you must have full access to the library. For more information, see [Library Access](library-access.md).

## Examples

The following example adds three media objects to the Windows Media Player media collection. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Adding a media object using a website.
player.mediaCollection.add("https://www.proseware.com/Media/Laure.wma");

// Adding a media object from a local network.
// Either use the @ symbol to denote a quoted string literal or add additional
// backlashes as an escape for every original backslash.
player.mediaCollection.add(@"\\yourservername\Public\Jeanne.wma");

// Adding a media object from a file on a local drive.
// Either use the @ symbol to denote a quoted string literal or add additional
// backlashes as an escape for every original backslash.
player.mediaCollection.add(@"C:\WMSDK\WMPSDK\samples\media\house.wma");
```


```VB

' Adding a media object using a website.
player.mediaCollection.add(&quot;http:&#39;www.proseware.com/Media/Laure.wma&quot;)

&#39; Adding a media object from a local network.
player.mediaCollection.add(&quot;\\yourservername\Public\Jeanne.wma&quot;)

&#39; Adding a media object from a file on a local drive.
player.mediaCollection.add(&quot;C:\WMSDK\WMPSDK\samples\media\house.wma&quot;)
```





## Requirements



|                      |                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection.remove (VB and C#)**](wmplibiwmpmediacollection-iwmpmediacollection-remove--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection.importPlaylist (VB and C#)**](wmplibiwmpplaylistcollection-iwmpplaylistcollection-importplaylist--vb-and-c.md)
</dt> </dl>

 

 





