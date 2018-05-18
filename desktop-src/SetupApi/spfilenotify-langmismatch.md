---
Description: 'The SPFILENOTIFY\_LANGMISMATCH notification is sent to the callback routine if the language of the file to be copied does not match the language of an existing target file.'
ms.assetid: 'dff3969e-5847-4ad5-b7d4-237144bbe8e6'
title: 'SPFILENOTIFY\_LANGMISMATCH message'
---

# SPFILENOTIFY\_LANGMISMATCH message

The **SPFILENOTIFY\_LANGMISMATCH** notification is sent to the callback routine if the language of the file to be copied does not match the language of an existing target file. It can be sent to the callback routine alone or combined, by using the OR operator, with [**SPFILENOTIFY\_TARGETEXISTS**](spfilenotify-targetexists.md) and/or [**SPFILENOTIFY\_TARGETNEWER**](spfilenotify-targetnewer.md).


```C++
SPFILENOTIFY_LANGMISMATCH
  Param1 = (UINT) FilePathInfo;
  Param2 = (UINT) LanguageInfo;
            
```



## Parameters

<dl> <dt>

*Param1* 
</dt> <dd>

Pointer to a [**FILEPATHS**](filepaths-str.md) structure that contains information about the paths of the source and target files.

</dd> <dt>

*Param2* 
</dt> <dd>

Identifies the mismatched languages. This member has the language identifier of the source file in the low word, and the language identifier of the existing target file in the high word.

</dd> </dl>

## Return value

The callback routine should return one of the following values.



| Return code                                                                          | Description                                                             |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**TRUE**</dt> </dl>  | Copy the file and overwrite the existing file.<br/>               |
| <dl> <dt>**FALSE**</dt> </dl> | Skip the copy operation. Do not overwrite the existing file.<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Setupapi.h</dt> </dl> |



## See also

<dl> <dt>

[Overview](overview.md)
</dt> <dt>

[Notifications](notifications.md)
</dt> <dt>

[**FILEPATHS**](filepaths-str.md)
</dt> <dt>

[**SetupCommitFileQueue**](setupcommitfilequeue.md)
</dt> <dt>

[**SetupDefaultQueueCallback**](setupdefaultqueuecallback.md)
</dt> <dt>

[**SetupInstallFile**](setupinstallfile.md)
</dt> <dt>

[**SetupInstallFileEx**](setupinstallfileex.md)
</dt> <dt>

[**SetupInstallFromInfSection**](setupinstallfrominfsection.md)
</dt> </dl>

 

 




