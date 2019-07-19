---
Description: 'Decrypts a message by using NTLM.'
ms.assetid: '44c63152-507d-4769-9c0c-d275d2b0deac'
title: 'DecryptMessage (NTLM) function'
---

# DecryptMessage (NTLM) function

The **DecryptMessage (NTLM)** function decrypts a message. Some packages do not encrypt and decrypt messages but rather perform and check an integrity [*hash*](security.h_gly#-security-hash-gly).

> [!Note]  
> [**EncryptMessage (NTLM)**](encryptmessage--ntlm.md) and **DecryptMessage (NTLM)** can be called at the same time from two different threads in a single [*Security Support Provider Interface*](security.s_gly#-security-security-support-provider-interface-gly) (SSPI) context if one thread is encrypting and the other is decrypting. If more than one thread is encrypting, or more than one thread is decrypting, each thread should obtain a unique context.

 

## Syntax


```C++
SECURITY_STATUS SEC_Entry DecryptMessage(
  _In_    PCtxtHandle    phContext,
  _Inout_ PSecBufferDesc pMessage,
  _In_    ULONG          MessageSeqNo,
  _Out_   PULONG         pfQOP
);
```



## Parameters

<dl> <dt>

*phContext* \[in\]
</dt> <dd>

A handle to the [*security context*](security.s_gly#-security-security-context-gly) to be used to decrypt the message.

</dd> <dt>

*pMessage* \[in, out\]
</dt> <dd>

A pointer to a [**SecBufferDesc**](secbufferdesc.md) structure. On input, the structure references one or more [**SecBuffer**](secbuffer.md) structures. At least one of these must be of type SECBUFFER\_DATA. That buffer contains the encrypted message. The encrypted message is decrypted in place, overwriting the original contents of its buffer.

</dd> <dt>

*MessageSeqNo* \[in\]
</dt> <dd>

The sequence number expected by the transport application, if any. If the transport application does not maintain sequence numbers, this parameter must be set to zero.

</dd> <dt>

*pfQOP* \[out\]
</dt> <dd>

A pointer to a variable of type **ULONG** that receives package-specific flags that indicate the quality of protection.

This parameter can be the following flag.



<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><thead><tr class="header"><th>Value</th><th>Meaning</th></tr></thead><tbody><tr class="odd"><td><span id="SECQOP_WRAP_NO_ENCRYPT"></span><span id="secqop_wrap_no_encrypt"></span><dl> <dt><strong>SECQOP_WRAP_NO_ENCRYPT</strong></dt> </dl></td><td>The message was not encrypted, but a header or trailer was produced.<br/><blockquote>[!Note]<br />
KERB_WRAP_NO_ENCRYPT has the same value and the same meaning.</blockquote><br/></td></tr></tbody></table>



 

</dd> </dl>

## Return value

If the function verifies that the message was received in the correct sequence, the function returns SEC\_E\_OK.

If the function fails to decrypt the message, it returns one of the following error codes.



| Return code                                                                                                | Description                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SEC\_E\_INCOMPLETE\_MESSAGE**</dt> </dl> | The data in the input buffer is incomplete. The application needs to read more data from the server and call [**DecryptMessage (NTLM)**](decryptmessage--ntlm.md) again.<br/> |
| <dl> <dt>**SEC\_E\_OUT\_OF\_SEQUENCE**</dt> </dl>   | The message was not received in the correct sequence.<br/>                                                                                                                      |



 

## Remarks

Sometimes an application will read data from the remote party, attempt to decrypt it by using **DecryptMessage (NTLM)**, and discover that **DecryptMessage (NTLM)** succeeded but the output buffers are empty. This is normal behavior, and applications must be able to deal with it.

**Windows XP:** This function was also known as **UnsealMessage**. Applications should now use **DecryptMessage (NTLM)** only.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Sspi.h (include Security.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Secur32.lib</dt> </dl>                 |
| DLL<br/>                      | <dl> <dt>Secur32.dll</dt> </dl>                 |



## See also

<dl> <dt>

[SSPI Functions](authentication-functions.md#sspi-functions)
</dt> <dt>

[**EncryptMessage (NTLM)**](encryptmessage--ntlm.md)
</dt> <dt>

[**SecBuffer**](secbuffer.md)
</dt> <dt>

[**SecBufferDesc**](secbufferdesc.md)
</dt> </dl>

 

 




