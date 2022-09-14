---
description: Shell.IsRestricted method - Retrieves a group's restriction setting from the registry.
ms.assetid: C4B3B5C0-7445-483a-885F-5283BD4D4B39
title: Shell.IsRestricted method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.IsRestricted
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.IsRestricted method

Retrieves a group's restriction setting from the registry.

## Syntax


```JScript
iRetVal = Shell.IsRestricted(
  sGroup,
  sRestriction
)
```


```VB

Shell.IsRestricted( _
  ByVal sGroup As BSTR, _
  ByVal sRestriction As BSTR _
) As Integer
```





## Parameters

<dl> <dt>

*sGroup* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the group name. This value is the name of a registry subkey under which to check for the restriction.

</dd> <dt>

*sRestriction* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the restriction whose value is to be retrieved.

</dd> </dl>

## Return value

### JScript

Type: **Integer\***

The value of the restriction. If the specified restriction is not found, the return value is 0.

### VB

Type: **Integer\***

The value of the restriction. If the specified restriction is not found, the return value is 0.

## Remarks

**IsRestricted** first looks for a subkey name that matches *sGroup* under the following key.

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Policies
```

Restrictions are declared as values of the individual policy subkeys. If the restriction named in *sRestriction* is found in the subkey named in *sGroup*, **IsRestricted** returns the restriction's current value. If the restriction is not found under **HKEY\_LOCAL\_MACHINE**, the same subkey is checked under **HKEY\_CURRENT\_USER**.

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **IsRestricted** to retrieve the data value of the **undockwithoutlogon** restriction from the **System** subkey. Usage is shown for JScript and VBScript.

JScript:


```JScript
<script language="JScript">
    function fnIsRestricedJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var lReturn;
        
        lReturn = objShell.IsRestricted("system", "undockwithoutlogon");
        document.write(lReturn);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnIsRestricedVB()
        dim objShell
        dim lReturn

        set objShell = CreateObject("shell.application")

        lReturn = objShell.IsRestricted("system", "undockwithoutlogon")
        document.write(lReturn)

        set objShell = nothing
    end function
</script>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
