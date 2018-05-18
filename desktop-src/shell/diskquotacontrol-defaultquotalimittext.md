---
Description: 'Gets the default quota limit as a text string.'
title: 'DiskQuotaControl.DefaultQuotaLimitText property'
---

# DiskQuotaControl.DefaultQuotaLimitText property

Gets the default quota limit as a text string.

This property is read-only.

## Syntax


```JScript
DefaultQuotaLimitText = DiskQuotaControl.DefaultQuotaLimitText
```



## Property value

A string value that contains the default quota limit for new users of the volume. For example, if the default quota is 10.5 MB, the value of the property is "10.5 MB". If the volume has no default quota, the property is set to "No Limit" or the localized equivalent.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DefaultQuotaLimit**](diskquotacontrol-defaultquotalimit.md)
</dt> <dt>

[**DiskQuotaControl**](diskquotacontrol-object.md)
</dt> </dl>

 

 




