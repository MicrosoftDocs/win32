---
title: IWMPCdromCollection count property
description: The count property gets the number of available CD and DVD drives on the system.
ms.assetid: 1359ab7e-fbe3-461c-801b-7c986f6e5687
keywords:
- count property Windows Media Player
- count property Windows Media Player , IWMPCdromCollection interface
- IWMPCdromCollection interface Windows Media Player , count property
topic_type:
- apiref
api_name:
- IWMPCdromCollection.count
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPCdromCollection::count property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **count** property gets the number of available CD and DVD drives on the system.

## Syntax


```CSharp
public System.Int32 count {get; set;}
```


```VB

Public ReadOnly Property count As System.Int32
```





## Property value

A **System.Int32** that is the count of available drives.

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

DVD drives are counted exactly like CD drives. However, the Windows Media Player ActiveX control only supports DVD functionality for Windows XP or later. Typically, DVD drives can play CD media, but CD drives cannot play DVD media.

## Examples

The following example uses count to display the number of available CD and DVD drives in a message box. The AxWMPLib.AxWindowsMediaPlayer object is represented by the variable named player.


```CSharp
// Store the number of available drives.
int numDrives = player.cdromCollection.count;

// Display the number of drives as a string.
System.Windows.Forms.MessageBox.Show("Number of available CD and DVD drives:  " + numDrives.ToString());
```


```VB

' Store the number of available drives.
Dim numDrives As Integer = player.cdromCollection.count

&#39; Display the number of drives as a string.
System.Windows.Forms.MessageBox.Show(&quot;Number of available CD and DVD drives:  &quot; + numDrives.ToString())
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromCollection Interface (VB and C#)**](iwmpcdromcollection--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





