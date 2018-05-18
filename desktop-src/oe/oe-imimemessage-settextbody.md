---
title: IMimeMessage SetTextBody method
description: Sets the text body for the message.
ms.assetid: 'fc3e8bda-486d-4492-99bf-406c50c63fbc'
keywords: ["SetTextBody method Windows Mail (formerly Outlook Express)", "SetTextBody method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , SetTextBody method"]
topic_type:
- apiref
api_name:
- IMimeMessage.SetTextBody
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::SetTextBody method

Sets the text body for the message.

## Syntax


```C++
HRESULT SetTextBody(
  [in]  DWORD        dwTxtType,
  [in]  ENCODINGTYPE ietEncoding,
  [in]  HBODY        hAlternative,
  [in]  IStream      *pStream,
  [out] LPHBODY      phBody
);
```



## Parameters

<dl> <dt>

*dwTxtType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the type of text body to retrieve.



| Value                                                                                                                                                                                                             | Meaning                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TXT_PLAIN"></span><span id="txt_plain"></span><dl> <dt>**TXT\_PLAIN**</dt> <dt>0x00000001</dt> </dl> | [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) is text/plain. <br/> |
| <span id="TXT_HTML"></span><span id="txt_html"></span><dl> <dt>**TXT\_HTML**</dt> <dt>0x00000002</dt> </dl>    | [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) is text/html. <br/>  |



 

</dd> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies an [**ENCODINGTYPE**](oe-encodingtype.md) value that indicates how the data in *pStream* should be encoded. Either **IET\_DECODED**, **IET\_BINARY**, **IET\_UNICODE**, or **IET\_INETCSET** is a typical value for this parameter.

</dd> <dt>

*hAlternative* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the alternate types of the text body in a message. On the first call to **IMimeMessage::SetTextBody**, this parameter should be **NULL**. On subsequent calls to **IMimeMessage::SetTextBody**, this parameter specifies the handle that was created from the previous call. MimeOLE uses this parameter to determine which multipart/alternative section to attach to the multiple types of text bodies.

</dd> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Receives an address to a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the text body. MimeOLE increments the reference count for this object and does not release it until the whole message object is freed or until [**HandsOffStorage**](oe-imimemessagetree-handsoffstorage.md) is called.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the new text body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                       |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                     |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pStream* is **NULL**. <br/>                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed.<br/>   |
| <dl> <dt>**MIME\_E\_INVALID\_TEXT\_TYPE**</dt> </dl> | Indicates that the value of *dwTxtType* is not valid. <br/> |



 

## Examples

This example illustrates how to create a simple message with HTML, a subject and a TO: line.


```C++
HRESULT MyCreateMessage(LPCTSTR pszPath, IStream ** ppStream)
{
   IMimeMessage * pMessage = NULL;
   HRESULT hr = MimeOleCreateMessage(NULL, &amp;pMessage);
   *ppStream = NULL;
   if (SUCCEEDED(hr))
   {
      IStream * pStreamTemp = NULL;
      HCHARSET hCharset;
      HBODY hBody = NULL;
      MimeOleSetBodyPropW(pMessage, HBODY_ROOT, PIDTOSTR(PID_HDR_SUBJECT), NOFLAGS, L"The Subject -- Welcome to my test email!!!");

      // Use IMimeAddressTable to add addresses one by one to the TO: line.
      // You can get the IMimeAddressTable interface using:
      // pMessage->BindToObject(HBODY_ROOT, IID_PPV_ARG(IMimePropertySet, 
      //                                                &amp;pPropertySet)))
      // pPropertySet->BindToObject(IID_PPV_ARG(IMimeAddressTable, 
      //                                        &amp;pAdrTable))).
      MimeOleSetBodyPropW(pMessage, HBODY_ROOT, PIDTOSTR(PID_HDR_FROM), 
                          NOFLAGS, L"MrSender@example.com");
      MimeOleSetBodyPropW(pMessage, HBODY_ROOT, PIDTOSTR(PID_HDR_TO), 
                          NOFLAGS, L"MrRecipient@example.com");

      // Set the bodies.
      // You can have inline images by calling IMimeMessage::AttachURL() 
      // with the inline image and then using the returned CID: URL 
      // in the HTML to reference the inline image.
      #define SZ_HTML_BODY L"<HTML> <BODY> <CENTER> Hi!!! </CENTER> <BR>
                             <BR> -Jo Brown </BODY> </HTML>"
      pStreamTemp = SHCreateMemStream((BYTE *)SZ_HTML_BODY, 
                             sizeof(SZ_HTML_BODY));
      if (pStreamTemp)
      {
         hr = pMessage->SetTextBody(TXT_HTML, IET_UNICODE, NULL, 
                                    pStreamTemp, &amp;hBody);
         pStreamTemp->Release();
      }
      #define SZ_TEXT_BODY L" Hi!!!\n\n\n -BryanSt"
      pStreamTemp = SHCreateMemStream((BYTE *)SZ_TEXT_BODY, 
                                              sizeof(SZ_TEXT_BODY));
      if (pStreamTemp)
      {
         hr = pMessage->SetTextBody(TXT_PLAIN, IET_UNICODE, hBody, 
                                               pStreamTemp, NULL);
         pStreamTemp->Release();
      }
      hr = pMessage->Commit(0);
      if (SUCCEEDED(hr))
      {
         hr = pMessage->GetMessageSource(ppStream, 0);
      }
      pMessage->Release();
   }
   return hr;
}
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





