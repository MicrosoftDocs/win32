---
title: D3DCompile2 function
description: Compiles Microsoft High Level Shader Language (HLSL) code into bytecode for a given target.
ms.assetid: 0CE217EA-44F4-4017-B2ED-95E8B122CA95
keywords:
- D3DCompile2 function HLSL
topic_type:
- apiref
api_name:
- D3DCompile2
api_location:
- D3DCompiler_47.dll
api_type:
- DllExport
ms.topic: article
ms.date: 05/31/2018
---

# D3DCompile2 function

Compiles Microsoft High Level Shader Language (HLSL) code into bytecode for a given target.

## Syntax

``` syntax
HRESULT WINAPI D3DCompile2(
  in      LPCVOID pSrcData,
  in      SIZE_T SrcDataSize,
  in_opt  LPCSTR pSourceName,
  in_opt  const D3D_SHADER_MACRO pDefines,
  in_opt  ID3DInclude pInclude,
  in      LPCSTR pEntrypoint,
  in      LPCSTR pTarget,
  in      UINT Flags1,
  in      UINT Flags2,
  in      UINT SecondaryDataFlags,
  in_opt  LPCVOID pSecondaryData,
  in      SIZE_T SecondaryDataSize,
  out     ID3DBlob ppCode,
  out_opt ID3DBlob ppErrorMsgs
);
```

## Parameters

<dl> <dt>

*pSrcData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to uncompiled shader data (ASCII HLSL code).

</dd> <dt>

*SrcDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The size, in bytes, of the block of memory that *pSrcData* points to.

</dd> <dt>

*pSourceName* \[in, optional\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

An optional pointer to a constant null-terminated string containing the name that identifies the source data to use in error messages. If not used, set to **NULL**.

</dd> <dt>

*pDefines* \[in, optional\]
</dt> <dd>

Type: **const [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732)\***

An optional array of [**D3D\_SHADER\_MACRO**](https://msdn.microsoft.com/library/windows/desktop/ff728732) structures that define shader macros. Each macro definition contains a name and a NULL-terminated definition. If not used, set to **NULL**.

</dd> <dt>

*pInclude* \[in, optional\]
</dt> <dd>

Type: **[**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746)\***

A pointer to an [**ID3DInclude**](https://msdn.microsoft.com/library/windows/desktop/ff728746) interface that the compiler uses to handle include files. If you set this parameter to **NULL** and the shader contains a \#include, a compile error occurs. You can pass the **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE** macro, which is a pointer to a default include handler. This default include handler includes files that are relative to the current directory and files that are relative to the directory of the initial source file. When you use **D3D\_COMPILE\_STANDARD\_FILE\_INCLUDE**, you must specify the source file name in the *pSourceName* parameter; the compiler will derive the initial relative directory from *pSourceName*.


```
#define D3D_COMPILE_STANDARD_FILE_INCLUDE ((ID3DInclude*)(UINT_PTR)1)
```



</dd> <dt>

*pEntrypoint* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to a constant null-terminated string that contains the name of the shader entry point function where shader execution begins. When you compile an effect, **D3DCompile2** ignores *pEntrypoint*; we recommend that you set *pEntrypoint* to **NULL** because it is good programming practice to set a pointer parameter to **NULL** if the called function will not use it.

</dd> <dt>

*pTarget* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to a constant null-terminated string that specifies the shader target or set of shader features to compile against. The shader target can be a shader model (for example, shader model 2, shader model 3, shader model 4, or shader model 5). The target can also be an effect type (for example, fx\_4\_1). For info about the targets that various profiles support, see [Specifying Compiler Targets](specifying-compiler-targets.md).

</dd> <dt>

*Flags1* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A combination of shader [**D3D compile constants**](d3dcompile-constants.md) that are combined by using a bitwise **OR** operation. The resulting value specifies how the compiler compiles the HLSL code.

</dd> <dt>

*Flags2* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A combination of effect [**D3D compile effect constants**](d3dcompile-effect-constants.md) that are combined by using a bitwise **OR** operation. The resulting value specifies how the compiler compiles the effect. When you compile a shader and not an effect file, **D3DCompile2** ignores *Flags2*; we recommend that you set *Flags2* to zero because it is good programming practice to set a nonpointer parameter to zero if the called function will not use it.

</dd> <dt>

*SecondaryDataFlags* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A combination of the following flags that are combined by using a bitwise **OR** operation. The resulting value specifies how the compiler compiles the HLSL code.



| Flag                                                  | Description                                                                                                                                |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| D3DCOMPILE\_SECDATA\_MERGE\_UAV\_SLOTS (0x01)         | Merge unordered access view (UAV) slots in the secondary data that the *pSecondaryData* parameter points to.                               |
| D3DCOMPILE\_SECDATA\_PRESERVE\_TEMPLATE\_SLOTS (0x02) | Preserve template slots in the secondary data that the *pSecondaryData* parameter points to.                                               |
| D3DCOMPILE\_SECDATA\_REQUIRE\_TEMPLATE\_MATCH (0x04)  | Require that templates in the secondary data that the *pSecondaryData* parameter points to match when the compiler compiles the HLSL code. |



 

If *pSecondaryData* is **NULL**, set to zero.

</dd> <dt>

*pSecondaryData* \[in, optional\]
</dt> <dd>

Type: **[**LPCVOID**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

A pointer to secondary data. If you don't pass secondary data, set to **NULL**. Use this secondary data to align UAV slots in two shaders. Suppose shader A has UAVs and they are bound to some slots. To compile shader B such that UAVs with the same names are mapped in B to the same slots as in A, pass A s byte code to **D3DCompile2** as the secondary data.

</dd> <dt>

*SecondaryDataSize* \[in\]
</dt> <dd>

Type: **[**SIZE\_T**](https://msdn.microsoft.com/library/windows/desktop/aa383751)**

The size, in bytes, of the block of memory that *pSecondaryData* points to. If *pSecondaryData* is **NULL**, set to zero.

</dd> <dt>

*ppCode* \[out\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access the compiled code.

</dd> <dt>

*ppErrorMsgs* \[out, optional\]
</dt> <dd>

Type: **[**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743)\*\***

A pointer to a variable that receives a pointer to the [**ID3DBlob**](https://msdn.microsoft.com/library/windows/desktop/ff728743) interface that you can use to access compiler error messages, or **NULL** if there are no errors.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/windows/desktop/aa383751#hresult)**

Returns one of the [Direct3D 11 return codes](https://msdn.microsoft.com/library/windows/desktop/ff476174).

## Remarks

The difference between **D3DCompile2** and [**D3DCompile**](d3dcompile.md) is that **D3DCompile2** takes some optional parameters (*SecondaryDataFlags*, *pSecondaryData* and *SecondaryDataSize*) that can be used to control some aspects of how bytecode is generated. Refer to the descriptions of these parameters for more details. There is no difference otherwise to the efficiency of the bytecode generated between **D3DCompile2** and **D3DCompile**.

### Compiling shaders for UWP

To compile offline shaders the recommend approach is to use the [Effect-Compiler Tool](https://msdn.microsoft.com/library/windows/desktop/bb232919.aspx). If you cannot compile all of your shaders ahead of time, consider compiling the more expensive ones and the ones on your startup and most performance-sensitive paths require, and compiling the rest at runtime. You can use a process similar to the following to compile a loaded or generated shader in a UWP application without blocking your user interface thread.

-   Using Visual Studio 2015+ to develop the UWP app, add the new item "shader.hlsl".
    -   In the **Solution Folder** view of Visual Studio, select the **shaders.hlsl** item, right-click for **Properties**.
    -   Make sure the item **Content** is set to **Yes**.
    -   Make sure the **Item Type** is set to **Text**.
    -   Add a button to XAML, name it appropriately ("TheButton" in this example), and add a **Click** handler.
-   Now add these includes to your .cpp file:

    ``` syntax
#include <ppltasks.h>
#include <d3dcompiler.h>
#include <Robuffer.h>
    ```

-   Use the following code to call **D3DCompile2**. Note that there is no error checking or handling here, and also that this code demonstrates you can do both I/O and compilation in the background, which leaves your UI more responsive.

    ``` syntax
    void App1::DirectXPage::TheButton_Click(Platform::Object^ sender, Windows::UI::Xaml::RoutedEventArgs^ e)
    {
      std::shared_ptr<Microsoft::WRL::ComPtr<ID3DBlob>> blobRef = std::make_shared<Microsoft::WRL::ComPtr<ID3DBlob>>();

      // Load a file and compile it.
      auto fileOp = Windows::ApplicationModel::Package::Current->InstalledLocation->GetFileAsync(L"shader.hlsl");
      create_task(fileOp).then([this](Windows::Storage::StorageFile^ file) -> IAsyncOperation<Windows::Storage::Streams::IBuffer^>^
      {
        // Do file I/O in background thread (use_arbitrary).
        return Windows::Storage::FileIO::ReadBufferAsync(file);
      }, task_continuation_context::use_arbitrary())
        .then([this, blobRef](Windows::Storage::Streams::IBuffer^ buffer)
      {
        // Do compilation in background thread (use_arbitrary).

        // Cast to Object^, then to its underlying IInspectable interface.
        Microsoft::WRL::ComPtr<IInspectable> insp(reinterpret_cast<IInspectable*>(buffer));

        // Query the IBufferByteAccess interface.
        Microsoft::WRL::ComPtr<Windows::Storage::Streams::IBufferByteAccess> bufferByteAccess;
        insp.As(&bufferByteAccess);

        // Retrieve the buffer data.
        byte *pBytes = nullptr;
        bufferByteAccess->Buffer(&pBytes);

        Microsoft::WRL::ComPtr<ID3DBlob> blob;
        Microsoft::WRL::ComPtr<ID3DBlob> errMsgs;
        D3DCompile2(pBytes, buffer->Length, "shader.hlsl", nullptr, nullptr, "main", "ps_5_0", 0, 0, 0, nullptr, 0, blob.GetAddressOf(), errMsgs.GetAddressOf());
        *blobRef = blob;
      }, task_continuation_context::use_arbitrary())
        .then([this, blobRef]()
      {
        // Update UI / use shader on foreground thread.
        wchar_t message[40];
        swprintf_s(message, L"blob is %u bytes long", (unsigned)(*blobRef)->GetBufferSize());
        this->TheButton->Content = ref new Platform::String(message);
      }, task_continuation_context::use_current());
    }
    ```

## Requirements



|                    |                                                                                                |
|--------------------|------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3Dcompiler.h</dt> </dl>       |
| Library<br/> | <dl> <dt>D3DCompiler.lib</dt> </dl>     |
| DLL<br/>     | <dl> <dt>D3DCompiler\_47.dll</dt> </dl> |



## See also

<dl> <dt>

[Functions](dx-graphics-d3dcompiler-reference-functions.md)
</dt> <dt>

[Specifying D3D12 Root Signatures in HLSL](https://msdn.microsoft.com/library/windows/desktop/dn913202)
</dt> </dl>

 

 





