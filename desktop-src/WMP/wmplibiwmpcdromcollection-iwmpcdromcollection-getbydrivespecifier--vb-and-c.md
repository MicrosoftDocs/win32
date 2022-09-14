---
title: IWMPCdromCollection getByDriveSpecifier method
description: The getByDriveSpecifier method returns an IWMPCdrom interface associated with a particular drive letter.
ms.assetid: 4a550eb1-a37e-43fd-9e08-801c4fd64e68
keywords:
- getByDriveSpecifier method Windows Media Player
- getByDriveSpecifier method Windows Media Player , IWMPCdromCollection interface
- IWMPCdromCollection interface Windows Media Player , getByDriveSpecifier method
topic_type:
- apiref
api_name:
- IWMPCdromCollection.getByDriveSpecifier
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromCollection::getByDriveSpecifier method

The **getByDriveSpecifier** method returns an **IWMPCdrom** interface associated with a particular drive letter.

## Syntax


```CSharp
public IWMPCdrom getByDriveSpecifier(
  System.String bstrDriveSpecifier
);
```


```VB

Public Function getByDriveSpecifier( _
  ByVal bstrDriveSpecifier As System.String _
) As IWMPCdrom
Implements IWMPCdromCollection.getByDriveSpecifier
```





## Parameters

<dl> <dt>

*bstrDriveSpecifier* \[in\]
</dt> <dd>

A **System.String** that is the drive letter followed by a colon (":") character.

</dd> </dl>

## Return value

A **WMPLib.IWMPCdrom** interface.

## Remarks

Drive letters must be given in the form *X*:, where *X* represents the drive letter.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following example uses **getByDriveSpecifier** to get the **IWMPCdrom** interface that corresponds to a drive letter provided by the user in a text box. The **IWMPCdrom.eject** method is then called to eject the specified drive. The **AxWMPLib.AxWindowsMediaPlayer** object is represented by the variable named player.


```CSharp
// Store the drive letter provided by the user.
string driveLetter = myText.Text;

// Append a colon to the drive letter to create a valid drive specifier.
driveLetter += ":";

// Get an IWMPCdrom interface for the drive.
WMPLib.IWMPCdrom drive = player.cdromCollection.getByDriveSpecifier(driveLetter);

// Use the eject method of the IWMPCdrom interface to open the drive door.
drive.eject();
```


```VB

' Store the drive letter provided by the user.
Dim driveLetter As String = myText.Text

&#39; Append a colon to the drive letter to create a valid drive specifier.
driveLetter += &quot;:&quot;

&#39; Get an IWMPCdrom interface for the drive.
Dim drive As WMPLib.IWMPCdrom = player.cdromCollection.getByDriveSpecifier(driveLetter)

&#39; Use the eject method of the IWMPCdrom interface to open the drive door.
drive.eject()
```





## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdrom Interface (VB and C#)**](iwmpcdrom--vb-and-c.md)
</dt> <dt>

[**IWMPCdrom.eject (VB and C#)**](wmplibiwmpcdrom-iwmpcdrom-eject--vb-and-c.md)
</dt> <dt>

[**IWMPCdromCollection Interface (VB and C#)**](iwmpcdromcollection--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





