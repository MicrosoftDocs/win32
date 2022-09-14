---
description: Shell.GetSetting method - Retrieves a global Shell setting.
ms.assetid: 3E8C7C6A-5696-4756-B4BF-902FA2420AE9
title: Shell.GetSetting method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.GetSetting
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.GetSetting method

Retrieves a global Shell setting.

## Syntax


```JScript
retVal = Shell.GetSetting(
  lSetting
)
```


```VB

Shell.GetSetting( _
  ByVal lSetting As long _
) As VARIANT_BOOL
```





## Parameters

<dl> <dt>

*lSetting* \[in\]
</dt> <dd>

Type: **long**

A value that specifies the current Shell setting to retrieve. Only one setting can be retrieved in each call. The following values are recognized by this method.

<dt>

<span id="SSF_AUTOCHECKSELECT"></span><span id="ssf_autocheckselect"></span>

<span id="SSF_AUTOCHECKSELECT"></span><span id="ssf_autocheckselect"></span>**SSF\_AUTOCHECKSELECT** (0x00800000)


</dt> <dd>

**Windows Vista and later**. The state of the **Use check boxes to select items** option. This option is enabled automatically when the system has a pen input device configured.

</dd> <dt>

<span id="SSF_DESKTOPHTML"></span><span id="ssf_desktophtml"></span>

<span id="SSF_DESKTOPHTML"></span><span id="ssf_desktophtml"></span>**SSF\_DESKTOPHTML** (0x00000200)


</dt> <dd>

Not used.

</dd> <dt>

<span id="SSF_DONTPRETTYPATH"></span><span id="ssf_dontprettypath"></span>

<span id="SSF_DONTPRETTYPATH"></span><span id="ssf_dontprettypath"></span>**SSF\_DONTPRETTYPATH** (0x00000800)


</dt> <dd>

The state of the **Allow all uppercase names** option. As of Windows Vista, this folder option is no longer available.

</dd> <dt>

<span id="SSF_DOUBLECLICKINWEBVIEW"></span><span id="ssf_doubleclickinwebview"></span>

<span id="SSF_DOUBLECLICKINWEBVIEW"></span><span id="ssf_doubleclickinwebview"></span>**SSF\_DOUBLECLICKINWEBVIEW** (0x00000080)


</dt> <dd>

The state of the **Double-click to open an item (single-click to select)** option.

</dd> <dt>

<span id="SSF_FILTER"></span><span id="ssf_filter"></span>

<span id="SSF_FILTER"></span><span id="ssf_filter"></span>**SSF\_FILTER** (0x00010000)


</dt> <dd>

Not used.

</dd> <dt>

<span id="SSF_HIDDENFILEEXTS"></span><span id="ssf_hiddenfileexts"></span>

<span id="SSF_HIDDENFILEEXTS"></span><span id="ssf_hiddenfileexts"></span>**SSF\_HIDDENFILEEXTS** (0x00000004)


</dt> <dd>

Not used.

</dd> <dt>

<span id="SSF_HIDEICONS"></span><span id="ssf_hideicons"></span>

<span id="SSF_HIDEICONS"></span><span id="ssf_hideicons"></span>**SSF\_HIDEICONS** (0x00004000)


</dt> <dd>

The state of icon display in the Windows Explorer list view. If this option is active, no icons are displayed in the list view.

</dd> <dt>

<span id="SSF_ICONSONLY"></span><span id="ssf_iconsonly"></span>

<span id="SSF_ICONSONLY"></span><span id="ssf_iconsonly"></span>**SSF\_ICONSONLY** (0x01000000)


</dt> <dd>

**Windows Vista and later**. The state of display name display in the Windows Explorer list view. If this option is active, icons are displayed in the list view, but display names are not.

</dd> <dt>

<span id="SSF_MAPNETDRVBUTTON"></span><span id="ssf_mapnetdrvbutton"></span>

<span id="SSF_MAPNETDRVBUTTON"></span><span id="ssf_mapnetdrvbutton"></span>**SSF\_MAPNETDRVBUTTON** (0x00001000)


</dt> <dd>

The state of the **Show map network drive button in toolbar** option. As of Windows Vista, this option is no longer available.

</dd> <dt>

<span id="SSF_NOCONFIRMRECYCLE"></span><span id="ssf_noconfirmrecycle"></span>

<span id="SSF_NOCONFIRMRECYCLE"></span><span id="ssf_noconfirmrecycle"></span>**SSF\_NOCONFIRMRECYCLE** (0x00008000)


</dt> <dd>

The state of the Recycle Bin's **Display delete confirmation dialog** option.

</dd> <dt>

<span id="SSF_NONETCRAWLING"></span><span id="ssf_nonetcrawling"></span>

<span id="SSF_NONETCRAWLING"></span><span id="ssf_nonetcrawling"></span>**SSF\_NONETCRAWLING** (0x00100000)


</dt> <dd>

The state of the **Automatically search for network folders and printers** option. As of Windows Vista, this option is no longer available.

</dd> <dt>

<span id="SSF_SEPPROCESS"></span><span id="ssf_sepprocess"></span>

<span id="SSF_SEPPROCESS"></span><span id="ssf_sepprocess"></span>**SSF\_SEPPROCESS** (0x00080000)


</dt> <dd>

The state of the **Launch folder windows in a separate process** option.

</dd> <dt>

<span id="SSF_SERVERADMINUI"></span><span id="ssf_serveradminui"></span>

<span id="SSF_SERVERADMINUI"></span><span id="ssf_serveradminui"></span>**SSF\_SERVERADMINUI** (0x00000004)


</dt> <dd>

Not used.

</dd> <dt>

<span id="SSF_SHOWALLOBJECTS"></span><span id="ssf_showallobjects"></span>

<span id="SSF_SHOWALLOBJECTS"></span><span id="ssf_showallobjects"></span>**SSF\_SHOWALLOBJECTS** (0x00000001)


</dt> <dd>

The state of the **Hidden files and folders** option.

</dd> <dt>

<span id="SSF_SHOWATTRIBCOL"></span><span id="ssf_showattribcol"></span>

<span id="SSF_SHOWATTRIBCOL"></span><span id="ssf_showattribcol"></span>**SSF\_SHOWATTRIBCOL** (0x00000100)


</dt> <dd>

The state of the **Show File Attributes in Detail View** option. As of Windows Vista, this option is no longer available.

</dd> <dt>

<span id="SSF_SHOWCOMPCOLOR"></span><span id="ssf_showcompcolor"></span>

<span id="SSF_SHOWCOMPCOLOR"></span><span id="ssf_showcompcolor"></span>**SSF\_SHOWCOMPCOLOR** (0x00000008)


</dt> <dd>

The state of the **Show encrypted or compressed NTFS files in color** option.

</dd> <dt>

<span id="SSF_SHOWEXTENSIONS"></span><span id="ssf_showextensions"></span>

<span id="SSF_SHOWEXTENSIONS"></span><span id="ssf_showextensions"></span>**SSF\_SHOWEXTENSIONS** (0x00000002)


</dt> <dd>

The state of the **Hide extensions for known file types** option.

</dd> <dt>

<span id="SSF_SHOWINFOTIP"></span><span id="ssf_showinfotip"></span>

<span id="SSF_SHOWINFOTIP"></span><span id="ssf_showinfotip"></span>**SSF\_SHOWINFOTIP** (0x00002000)


</dt> <dd>

The state of the **Show pop-up description for folder and desktop items** option.

</dd> <dt>

<span id="SSF_SHOWSTARTPAGE"></span><span id="ssf_showstartpage"></span>

<span id="SSF_SHOWSTARTPAGE"></span><span id="ssf_showstartpage"></span>**SSF\_SHOWSTARTPAGE** (0x00400000)


</dt> <dd>

Not used.

</dd> <dt>

<span id="SSF_SHOWSUPERHIDDEN"></span><span id="ssf_showsuperhidden"></span>

<span id="SSF_SHOWSUPERHIDDEN"></span><span id="ssf_showsuperhidden"></span>**SSF\_SHOWSUPERHIDDEN** (0x00040000)


</dt> <dd>

The state of the **Hide protected operating system files** option.

</dd> <dt>

<span id="SSF_SHOWSYSFILES"></span><span id="ssf_showsysfiles"></span>

<span id="SSF_SHOWSYSFILES"></span><span id="ssf_showsysfiles"></span>**SSF\_SHOWSYSFILES** (0x00000020)


</dt> <dd>

The state of the **Hidden files and folders** option. In Windows Vista and later, this is equivalent to SSF\_SHOWALLOBJECTS. In versions of Windows before Windows Vista, this value referred to the state of the **Do not show hidden files and folders** option.

</dd> <dt>

<span id="SSF_SHOWTYPEOVERLAY"></span><span id="ssf_showtypeoverlay"></span>

<span id="SSF_SHOWTYPEOVERLAY"></span><span id="ssf_showtypeoverlay"></span>**SSF\_SHOWTYPEOVERLAY** (0x02000000)


</dt> <dd>

**Windows Vista and later**. The state of the **Display file icon on thumbnails** option. If this option is active, a file type overlay is applied when a file supplies a thumbnail representation.

</dd> <dt>

<span id="SSF_SORTCOLUMNS"></span><span id="ssf_sortcolumns"></span>

<span id="SSF_SORTCOLUMNS"></span><span id="ssf_sortcolumns"></span>**SSF\_SORTCOLUMNS** (0x00000010)


</dt> <dd>

Not used.

</dd> <dt>

<span id="SSF_STARTPANELON"></span><span id="ssf_startpanelon"></span>

<span id="SSF_STARTPANELON"></span><span id="ssf_startpanelon"></span>**SSF\_STARTPANELON** (0x00200000)


</dt> <dd>

The state of the Windows XP display option, which selects between the Windows XP style and the classic style. As of Windows Vista, this option is no longer available.

</dd> <dt>

<span id="SSF_WEBVIEW"></span><span id="ssf_webview"></span>

<span id="SSF_WEBVIEW"></span><span id="ssf_webview"></span>**SSF\_WEBVIEW** (0x00020000)


</dt> <dd>

The state of the **Display as a web view option**. As of Windows Vista, this option is no longer available.

</dd> <dt>

<span id="SSF_WIN95CLASSIC"></span><span id="ssf_win95classic"></span>

<span id="SSF_WIN95CLASSIC"></span><span id="ssf_win95classic"></span>**SSF\_WIN95CLASSIC** (0x00000400)


</dt> <dd>

The state of the **Classic Style** option. As of Windows Vista, this option is no longer available.

</dd> </dl> </dd> </dl>

## Return value

### JScript

Type: **VARIANT\_BOOL\***

Set to **true** if the setting exists; otherwise, **false**.

### VB

Type: **VARIANT\_BOOL\***

Set to **true** if the setting exists; otherwise, **false**.

## Examples

The following examples show the use of **GetSetting** for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JavaScript">
    function fnIShellDispatch4GetSettingJ()
    {
        var objIShellDispatch4 = new ActiveXObject("Shell.Application");
        var vReturn;
        var ssfSHOWALLOBJECTS = 1;

        vReturn = objIShellDispatch4.GetSetting(ssfSHOWALLOBJECTS);
        alert(vReturn);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnIShellDispatch4GetSettingVB()
        dim objIShellDispatch4
        
        set objIShellDispatch4 = CreateObject("Shell.Application")
        if (not objIShellDispatch4 is nothing) then
            dim vReturn
            dim ssfSHOWALLOBJECTS
            
            ssfSHOWALLOBJECTS = 1
            vReturn = objIShellDispatch4.GetSetting(ssfSHOWALLOBJECTS)
            alert(vReturn)
        end if
        set objIShellDispatch4 = nothing
    end function
```



Visual Basic:


```VB
Private Sub fnIShellDispatch4GetSetting()
    Dim objIShellDispatch4 As Shell
    
    Set objIShellDispatch4 = New Shell
    If (Not objIShellDispatch4 Is Nothing) Then
        Dim vReturn As Variant
        Dim ssfSHOWALLOBJECTS As Long
        
        ssfSHOWALLOBJECTS = 1
        vReturn = objIShellDispatch4.GetSetting(ssfSHOWALLOBJECTS)
        Debug.Print vReturn
    End If
    Set objIShellDispatch4 = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



 

 




