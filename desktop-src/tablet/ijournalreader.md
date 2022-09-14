---
description: Provides read access to a Windows Journal file, returning a stream containing an XML version of the file's contents.
ms.assetid: e4e19f69-6377-4f06-856d-7f9b453e7656
title: IJournalReader interface (Journal.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IJournalReader
api_type: 
- COM
api_location: 
- Journal.dll
---

# IJournalReader interface

Provides read access to a Windows Journal file, returning a stream containing an XML version of the file's contents.

> [!Note]  
> The Journal Reader component cannot read Windows Journal files created by machines running Windows 7 or later. The IJournalReader interface should be considered deprecated or obsolete and should not be used.

 

## Members

The **IJournalReader** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IJournalReader** also has these types of members:

-   [Methods](#methods)

### Methods

The **IJournalReader** interface has these methods.



| Method                                                  | Description                                                                                                           |
|:--------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**ReadFromStream**](ijournalreader-readfromstream.md) | Takes a stream to a Journal Note file and returns an XML stream representing the contents of the document.<br/> |



 

## Remarks

The **JournalReader** class enables you to load a Journal document stream and to receive an XML stream representing the contents. You can reconstitute, display, and manipulate the ink.

## Examples

The following example of a handler for a button's [**Click**](/dotnet/api/system.windows.forms.control.click?view=netcore-3.1&preserve-view=true) event creates an instance of the **JournalReader** class and uses it to read an existing Journal file.

> [!Note]  
> The **DisplayXml** method called from this example is not shown. The specific implementation of such a method is dependent on your application's needs.

 


```C++
void CJntlReaderMFCDlg::OnBnClickedButton1()
{
  static TCHAR BASED_CODE szFilter[] = 
    _T("Journal files (*.jnt)|*.jnt|All files (*.*)|*.*");
  CFileDialog* fileDialog = new CFileDialog(TRUE, _T("*.jnt"), NULL, 
                                 OFN_FILEMUSTEXIST, szFilter, this);

  // Get the filename from the user via a File Open dialog
  if (fileDialog != NULL &&
      fileDialog->DoModal() == IDOK)
  {
    CString strFileName = fileDialog->GetPathName();

    // Read a JNT file into a memory buffer
    HANDLE hFile = CreateFile(strFileName,
                              GENERIC_READ,
                              FILE_SHARE_READ,
                              NULL,
                              OPEN_EXISTING,
                              FILE_ATTRIBUTE_NORMAL,
                              NULL);
    
    if (hFile != INVALID_HANDLE_VALUE)
    {
      // Allocate memory to hold the file contents
      DWORD dwFileSize = GetFileSize(hFile, NULL);
      HGLOBAL hGlobal = GlobalAlloc(GHND, dwFileSize);

      if (hGlobal != NULL)
      {
        LPBYTE pData = (LPBYTE)GlobalLock(hGlobal);

        if (pData != NULL)
        {
          DWORD dwRead;

          // Read the Journal file into the pData buffer
          if (ReadFile(hFile, pData, dwFileSize, &dwRead, NULL) &&
              (dwRead == dwFileSize))
          {
            HRESULT hr;
            IStream* pJntStream;

            // Create an IStream that points to the buffer
            hr = CreateStreamOnHGlobal(hGlobal, FALSE, &pJntStream);

            if (SUCCEEDED(hr))
            {
              IJournalReader* pJntReader;

              // Create a JournalReader object
              hr = CoCreateInstance(CLSID_JournalReader, NULL, CLSCTX_ALL, 
                          IID_IJournalReader, (void**)&pJntReader);

              if (SUCCEEDED(hr))
              {
                IStream* pXmlStream;

                // Read in the JNT file via the JournalReader
                hr = pJntReader->ReadFromStream(pJntStream, &pXmlStream);

                if (SUCCEEDED(hr))
                {
                  // Display results
                  DisplayXml(pXmlStream);

                  // Clean up
                  pXmlStream->Release();
                }
                pJntReader->Release();
              }
              pJntStream->Release();
            }
          }
          GlobalUnlock(hGlobal);
        }
        GlobalFree(hGlobal);
      }
      CloseHandle(hFile);
    }
    delete fileDialog;
  }
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                     |
| Minimum supported server<br/> | None supported<br/>                                                                                         |
| Header<br/>                   | <dl> <dt>Journal.h (also requires journal\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Journal.dll</dt> </dl>                            |



## See also

<dl> <dt>

[Custom Property GUIDs](custom-property-guids.md)
</dt> <dt>

[**ReadFromStream Method**](ijournalreader-readfromstream.md)
</dt> </dl>

 

