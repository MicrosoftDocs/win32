---
description: Describes the DirectX SDK's inclusion in the Windows SDK and provides a list of technologies and tools that are now included in the Windows SDK.
ms.assetid: d8765da9-e7cf-47e8-8bc3-4b29162da41b
title: Where is the DirectX SDK?
ms.topic: article
ms.date: 05/31/2018
---

# Where is the DirectX SDK?

Starting with Windows 8, the DirectX SDK is included as part of the Windows SDK.

We originally created the DirectX SDK as a high-performance platform for game development on top of Windows. As DirectX technologies matured, they became relevant to a broader range of applications. Today, the availability of Direct3D hardware in computers drives even traditional desktop applications to use graphics hardware acceleration. In parallel, DirectX technologies are more integrated with Windows. DirectX is now a fundamental part of Windows.

Because the Windows SDK is the primary developer SDK for Windows, DirectX is now included in it. You can now use the Windows SDK to build great games for Windows. To download the Windows 11 SDK, Windows 10 SDK, or Windows 8.x SDK see [Windows SDK and emulator archive](https://developer.microsoft.com/windows/downloads/sdk-archive).

The following technologies and tools, formerly part of the DirectX SDK, are now part of the Windows SDK.


| Technology or tool | Description | 
|--------------------|-------------|
| <span id="Windows_Graphics_Components"></span><span id="windows_graphics_components"></span><span id="WINDOWS_GRAPHICS_COMPONENTS"></span>Windows Graphics Components<br /> | The headers and libraries for <a href="/windows/desktop/direct3d">Direct3D</a> and other Windows graphics APIs, like <a href="/windows/desktop/Direct2D/direct2d-portal">Direct2D</a>, are available in the Windows SDK. <br /><blockquote>[!Note]<br />The deprecated D3DX9/D3DX10/D3DX11 utility libraries are available via <a href="https://www.nuget.org/packages/Microsoft.DXSDK.D3DX">NuGet</a>, but there are also a number of <a href="https://walbourn.github.io/living-without-d3dx/">open source alternatives</a>. The D3DCSX DirectCompute utility library and redistributable DLL is available in the Windows SDK. D3DX12 is available on <a href="https://github.com/microsoft/DirectX-Headers">GitHub</a>.</blockquote><br /> | 
| <span id="HLSL_compiler__FXC.EXE_"></span><span id="hlsl_compiler__fxc.exe_"></span><span id="HLSL_COMPILER__FXC.EXE_"></span>HLSL compiler (FXC.EXE)<br /> | The <a href="/windows/desktop/direct3dhlsl/dx-graphics-hlsl">HLSL</a> compiler is a tool in the appropriate architecture subdirectory under the bin folder in the Windows SDK.<br /><blockquote>[!Note]<br />The D3DCompiler API and redistributable DLL is available in the Windows SDK.</blockquote><br /><br />For DirectX 12 development, use the DXCompiler in the Windows SDK and hosted on [GitHub](https://github.com/Microsoft/DirectXShaderCompiler).<br /> | 
| <span id="PIX_for_"></span><span id="pix_for_"></span><span id="PIX_FOR_"></span>PIX for Windows<br /> | A replacement for the PIX for Windows tool is now a feature in Microsoft Visual Studio, called Visual Studio Graphics Debugger. This feature has greatly improved usability, support for Windows 8, and Direct3D 11.1, and integration with traditional Microsoft Visual Studio features such as call stacks and debugging windows for <a href="/windows/desktop/direct3dhlsl/dx-graphics-hlsl">HLSL</a> debugging. For more info about this new feature, see <a href="/visualstudio/debugger/visual-studio-graphics-diagnostics">Debugging DirectX Graphics</a>.<br /><br />For DirectX 12 development, see the latest generation of <a href="https://devblogs.microsoft.com/pix/">PIX on Windows</a><br /> | 
| <span id="XAudio2_for_"></span><span id="xaudio2_for_"></span><span id="XAUDIO2_FOR_"></span><a href="/windows/desktop/xaudio2/xaudio2-apis-portal">XAudio2</a> for Windows<br /> | The <a href="/windows/desktop/xaudio2/xaudio2-apis-portal">XAudio2</a> API is now a system component in Windows 11, Windows 10, and Windows 8.x. The headers and libraries for XAudio2 are available in the Windows SDK. For Windows 7 support, see <a href="/windows/win32/xaudio2/xaudio2-redistributable">XAudio2Redist</a>.<br /> | 
| <span id="XInput_for_"></span><span id="xinput_for_"></span><span id="XINPUT_FOR_"></span><a href="/windows/desktop/xinput/xinput-game-controller-apis-portal">XInput</a> for Windows<br /> | The <a href="/windows/desktop/xinput/xinput-game-controller-apis-portal">XInput</a> 1.4 API is now a system component in Windows 11, Windows 10, and Windows 8.x. The headers and libraries for XInput are available in the Windows SDK.<br /><blockquote>[!Note]<br />Legacy XInput 9.1.0 is also available as part of Windows 7 or later.</blockquote><br /> | 
| <span id="XNAMATH"></span><span id="xnamath"></span>XNAMATH<br /> | The most recent version of XNAMATH, which is updated for new instruction sets as well as ARM/ARM64, is now <a href="/windows/desktop/dxmath/directxmath-portal">DirectXMath</a>. The headers for DirectXMath are available in the Windows SDK and on <a href="https://github.com/Microsoft/DirectXMath">GitHub</a>.<br /> | 
| <span id="DirectX_Control_Panel_and_DirectX_Capabilities_Viewer"></span><span id="directx_control_panel_and_directx_capabilities_viewer"></span><span id="DIRECTX_CONTROL_PANEL_AND_DIRECTX_CAPABILITIES_VIEWER"></span>DirectX Control Panel and DirectX Capabilities Viewer<br /> | The DirectX Control Panel and DirectX Capabilities Viewer utilities are included in the appropriate architecture subdirectory under the bin folder in the Windows SDK. DirectX Capabilities Viewer is also available on <a href="https://github.com/microsoft/DxCapsViewer">GitHub</a>.<br /> | 
| <span id="XACT"></span><span id="xact"></span>XACT<br /> | The Xbox Audio Cross Platform Tool (XACT) is no longer supported for use on Windows.<br /> | 
| <span id="Games_Explorer_and_GDFMAKER"></span><span id="games_explorer_and_gdfmaker"></span><span id="GAMES_EXPLORER_AND_GDFMAKER"></span><a href="/previous-versions/windows/desktop/legacy/hh437965(v=vs.85)">Games Explorer</a> and GDFMAKER<br /> | The <a href="/previous-versions/windows/desktop/legacy/hh437965(v=vs.85)">Games Explorer</a> API presents games to users of Windows. The Games Explorer API is supported only on Windows Vista and Windows 7. Use the Games Definition File Maker tool (GDFMAKER.EXE) to declare game ratings for Windows Store apps. <br /> The Game Definition File Maker tool (GDFMaker.exe) is included in the x86 subdirectory under the bin folder in the Windows SDK, and supports both Windows Store apps and Win32 desktop applications.<br /><br /> | 
| <span id="Tools"></span><span id="tools"></span><span id="TOOLS"></span>Other DirectX SDK Tools<br /> | Miscellaneous tools such as dxtex.exe, meshconvert.exe, texconv.exe, and uvatlas.exe can be found online. For more info about these tools, see <a href="https://walbourn.github.io/directx-sdk-tools-catalog/">DirectX SDK Tools Catalog</a>.<br /> |
| <span id="Samples"></span><span id="samples"></span><span id="SAMPLES"></span>Samples<br /> | You can find sample applications that highlight DirectX 12 technologies on Windows in the <a href="https://github.com/Microsoft/DirectX-Graphics-Samples">DirectX samples</a> repo. Most samples for older versions of Direct3D are also available online. For more info about these samples, see <a href="https://walbourn.github.io/directx-sdk-samples-catalog/">DirectX SDK Samples Catalog</a>.<br /> | 
| <span id="Managed_DirectX_1.1"></span><span id="managed_directx_1.1"></span><span id="MANAGED_DIRECTX_1.1"></span>Managed DirectX 1.1<br /> | The .NET DirectX assemblies are deprecated and are not recommended for use by new applications. There are a number of alternatives available. See <a href="https://walbourn.github.io/directx-and-net/">DirectX and .NET</a>. <br /> | 




 

The legacy DirectX SDK is available for download from [Microsoft Download Center](https://go.microsoft.com/fwlink/?LinkId=226640) if required, but use for new projects is not recommended.

> [!Note]  
> The DirectX SDK fails to install if you have a certain version of the Visual C++ 2010 Redistributable Package already installed. For more info about and a solution to fix this issue, see ["S1023" error when you install the DirectX SDK (June 2010)](https://support.microsoft.com/kb/2728613).

 

## Using DirectX SDK projects with Visual Studio

The samples from the June 2010 DirectX SDK are supported with premium Visual Studio SKUs (Microsoft Visual Studio Professional 2012, Microsoft Visual Studio Ultimate 2012, Microsoft Visual Studio Professional 2013, or Microsoft Visual Studio Ultimate 2013) on Windows 7 and the Windows 8 and later releases. Due to the transition of DirectX headers and libraries into the Windows SDK, changes to the project settings are needed to build these samples correctly with how the Windows 8 SDK and later is packaged with the premium Visual Studio SKUs.

These steps also apply to your own projects that are dependent on the DirectX SDK.

1.  Ensure that the June 2010 release of the DirectX SDK is installed on your development computer. If you install onto a computer running Windows 8 and later, you will be prompted and required to enable .NET 3.5 as a prerequisite installation to the DirectX SDK.

    > [!Note]  
    > The DirectX SDK fails to install if you have a certain version of the Visual C++ 2010 Redistributable Package already installed. For more info about and a solution to fix this issue, see ["S1023" error when you install the DirectX SDK (June 2010)](https://support.microsoft.com/kb/2728613).

     

2.  Make sure that you are using one of the premium Visual Studio SKUs. Microsoft Visual Studio Express 2012 for Windows 8 or Microsoft Visual Studio Express 2013 for Windows won't build Windows 8 and later desktop applications such as the DirectX SDK samples. To install one of the premium Visual Studio SKUs, go to: [Visual Studio downloads](https://www.microsoft.com/visualstudio/11/downloads) and follow the instructions.

3.  Use the DirectX SDK Sample Browser to install the project files for the desired sample. Open the sample’s Microsoft Visual Studio 2010 compatible solution file (suffixed with **\_2010**).

4.  If you are opening the sample on a system that only has Microsoft Visual Studio 2012 or Microsoft Visual Studio 2013 installed, you get the following message: "This solution contains one or more projects using an earlier version of VC++ compiler and libraries. Each project can be updated to use the VC++ compiler and libraries (v110)." Choose the **Update** option from this dialog box to update before you open the project.

    Otherwise, you can update to the Visual Studio 2012 or Visual Studio 2013 C++ 11 compiler and libraries after they have loaded by right-clicking on the solution and choosing **Update VC++ projects**.

5.  D3DX is not considered the canonical API for using Direct3D in Windows 8 and later and therefore isn't included with the corresponding Windows SDK. Investigate alternate solutions for working with the Direct3D API. For legacy projects, such as the Windows 7 (and earlier) DirectX SDK samples, the following steps are necessary to build applications with D3DX using the DirectX SDK:

    1.  Modify the project’s **VC++** directories as follows to use the right order for SDK headers and libraries.

        <dl> i. Open **Properties** for the project and select the **VC++ Directories** page.  
        ii. Select **All Configurations and All Platforms**.  
        iii. Set these directories as follows:

        -   Executable Directories: **\<inherit from parent or project defaults\>** (On right-side drop-down)
        -   Include Directories: **$(IncludePath);$(DXSDK\_DIR)Include**
        -   Include Library Directories: **$(LibraryPath);$(DXSDK\_DIR)Lib\\x86**

          
        iv. Click **Apply**.  
        v. Choose the **x64 Platform**.  
        vi. Set the **Library Directory** as follows:

        -   Library Directories: **$(LibraryPath);$(DXSDK\_DIR)Lib\\x64**

          
        </dl>

    2.  Wherever "d3dx9.h", "d3dx10.h", or "d3dx11.h" are included in your project, be sure to explicitly include "d3d9.h", "d3d10.h" and "dxgi.h", or "d3d11.h" and "dxgi.h" first to ensure you are picking up the newer version. You can disable **warning C4005** if needed; however, this warning indicates you are using the older version of these headers.
    3.  Remove all references to DXGIType.h in your project. This header doesn't exist in the Windows SDK, and the DirectX SDK version conflicts with the new winerror.h.
    4.  All D3DX DLLs are installed onto your development computer by the DirectX SDK installation. Ensure that the necessary D3DX dependencies are redistributed with any sample or with your application if it is moved to another machine.
    5.  Be aware that replacement technologies for current uses of D3DX11 include [DirectXTex](https://github.com/Microsoft/DirectXTex), [DirectXTK](https://github.com/Microsoft/DirectXTK), [DirectXMesh](https://github.com/Microsoft/DirectXMesh), and [UVAtlas](https://github.com/Microsoft/UVAtlas). D3DXMath is replaced by [DirectXMath](./dxmath/directxmath-portal.md).

6.  Ensure that you are using the new version of the HLSL shader compiler by observing the following conditions:

    1.  Changing the executable directory as per step 5 will cause project builds to use FXC from the Windows SDK install. Be aware that HLSL files are now officially recognized by Visual Studio. You can add them as project files and set compiler options through the project system.

    2.  Invoking run-time compilation through the legacy D3DX DLL will use the incorrect older version of the HLSL compiler. Replace all references to D3DXCompile\*, D3DX10Compile\*, and D3DX11Compile\* APIs in your code with the D3DCompile function in D3DCOMPILER\_46.DLL or D3DCOMPILER\_47.DLL.

    3.  Any project that uses run-time shader compilation must have D3DCOMPILER\_xx.DLL copied to the local executable path for the project. This DLL is available in this sub-directory of the Windows SDK installation under **%ProgramFiles(x86)%\\Windows Kits\\8.0\\Redist\\D3D\\&lt;arch&gt;** or **%ProgramFiles(x86)%\\Windows Kits\\8.1\\Redist\\D3D\\&lt;arch&gt;** where **&lt;arch&gt;** is **x86** and **x64**.

        The D3DCOMPILER\_46.DLL or D3DCOMPILER\_47.DLL from the Windows SDK is not a system component and should not be copied to the Windows system directory. You can redistribute this DLL to other computers with your application as a side-by-side DLL.

7.  Any project that uses the XInput API and is intended to run on Windows 7 or older versions of Windows need to use either the legacy version (9.1.0) or will need to explicitly include the headers and libraries for this component from the DirectX SDK. The XInput header and XINPUT.LIB that are included in the Windows SDK target only the version (1.4) that ship as part of Windows 8 and later. The same header can be used with XINPUT9\_1\_0.LIB to use the legacy version, which is included with older versions of Windows. The legacy version of XInput doesn't detect full capabilities or support controller-integrated audio, so if support for these features is required, you must use the DirectX SDK version (1.3).

    To use the full-featured down-level XInput API, you should `#include` the specific XInput headers from the DirectX SDK directly:

    `#include <%DXSDK_DIR%Include\xinput.h>`

    ...and in your linker options for Additional Dependencies, link directly to the DirectX SDK XInput library:

    **%DXSDK\_DIR%Include\\&lt;arch&gt;\\xinput.lib**

    The XINPUT1\_3.DLL binary is installed to the Windows system directories by the DirectX SDK installation on your development computer. You will need to redistribute this binary with your application using the DirectX Setup installation from the DirectX SDK.

8.  Any project that uses the XAudio2 API and is intended to run on Windows 7 or older versions of Windows need to use either the older version (9.1.0) or explicitly include the headers and libraries for this component from the DirectX SDK. The XAudio2 headers and libraries that are included with the Windows SDK target only the version (2.8) that is included as part of Windows 8.

    For example, with XAudio2, you should `#include` the specific XAudio2 headers from the DirectX SDK directly:

    `  #include <%DXSDK_DIR%Include\xaudio2.h> `

    ...and in your linker options for Additional Dependencies, link directly to the DirectX SDK XAudio2 library:

    **%DXSDK\_DIR%Include\\&lt;arch&gt;\\xaudio2.lib**

    The XAUDIO2\_7.DLL binary is installed to the Windows system directories by the DirectX SDK installation on your development computer. You need to redistribute these libraries with your application using the DirectX Setup installation from the DirectX SDK.

9.  If you’ve used the DirectX SDK with past versions of Visual Studio, the Visual Studio 2010 upgrade might have migrated the DirectX SDK path into your default project settings. It is recommended that you remove these settings to prevent future build errors. In the **%USERPROFILE%\\AppData\\Local\\Microsoft\\MSBuild\\v4.0** directory, modify the **Microsoft.Cpp.Win32.user** and **Microsoft.Cpp.x64.user** files to remove all references to DXSDK\_DIR paths. Alternatively, you can remove the entire &lt;PropertyGroup&gt; node that contains the Path entries such as &lt;ExecutablePath&gt; and &lt;IncludePath&gt; to revert to standard defaults. If you don’t see references to DXSDK\_DIR in these files, no changes are necessary.

10. If the resulting app supports Windows Vista with Service Pack 2 (SP2) as well as Windows 7 and Windows 8 and later, set the Preprocessor Definition named **\_WIN32\_WINNT** to 0x600. If it only supports Windows 7 and Windows 8 and later, set it to 0x601.

    For example:

    1.  Open **Properties** for the project and select **C/C++** > **Preprocessor**.
    2.  Select **All Configurations** and **All Platforms**.
    3.  Go to the **Preprocessor Definitions** section and set \_WIN32\_WINNT=0x600.
    4.  Click **Apply**.

## Related topics

<dl> <dt>

**Games for Windows and the DirectX SDK**
</dt> <dt>

[Where is the DirectX SDK (2021 Edition)?](https://walbourn.github.io/where-is-the-directx-sdk-2021-edition/)
</dt> <dt>

[DirectX SDKs of a certain age](https://walbourn.github.io/directx-sdks-of-a-certain-age/)
</dt> <dt>

[Living without D3DX](https://walbourn.github.io/living-without-d3dx/)
</dt> </dl> 
