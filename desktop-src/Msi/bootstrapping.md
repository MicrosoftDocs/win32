---
description: Currently every installation that attempts to use the Windows Installer begins by checking whether the installer is present on the user's computer, and if it is not present, whether the user and computer are ready to install Windows Installer.
ms.assetid: a5174284-2a8c-4510-accf-641fda5be98d
title: Bootstrapping
ms.topic: article
ms.date: 05/31/2018
---

# Bootstrapping

Currently every installation that attempts to use the Windows Installer begins by checking whether the installer is present on the user's computer, and if it is not present, whether the user and computer are ready to install Windows Installer. A setup application [Instmsi.exe](instmsi-exe.md) is available with the Windows Installer SDK that contains all logic and functionality to install Windows Installer. However, a bootstrapping application must manage this installation.

The bootstrapping application must first check to see whether Windows Installer is currently installed. Applications can get the version of Windows Installer currently installed by using [**DllGetVersion**](/windows/win32/api/shlwapi/nc-shlwapi-dllgetversionproc). If Windows Installer is not currently installed, the bootstrapping application must query the operating system to determine which version of the Instmsi.exe is required. Once the installation of Windows Installer has initiated, the bootstrapping application must handle return codes from the Instmsi.exe application and handle any reboot that is incurred during the Windows Installer installation. For more information, see [Determining the Windows Installer Version](determining-the-windows-installer-version.md)

The following example demonstrates how the setup application which installs Microsoft Office 2000 checks the user's system and configures the Windows Installer installation. This example is specifically written to install Office 2000 and should be used as a general reference only.

When a user inserts an Office 2000 CD-ROM into their computer, Setup.exe attempts to launch the maintenance mode, the setup application, or does nothing at all, according to the user's needs. The following section describes how the Office 2000 setup application, named Setup.exe, qualifies the user and their computer, constructs a command line and installs Windows Installer using the Msiexec.exe application.

## How Setup.exe Bootstraps the Windows Installer when Installing Office 2000

1.  The user inserts an Office 2000 CD-ROM into their computer. The Windows operating system initiates Setup.exe using the /autorun switch and the Autorun.inf file. The Autorun.inf file is found at the root of the Office 2000 CD-ROM and contains the following sections:

    \[Autorun\]

     

    \[Office Features\]

     

    \[Product Information\]

     

    \[ServicePack\].

    The \[Autorun\] section contains a command line that executes the Setup.exe application, executes the icon used to display the disc, and contains information to add an "Install" option and a "Configure" option to the context menu for the CD-ROM.

    The \[Office Features\] section contains a list of features and feature name pairs.

    The \[Product Information\] section specifies the name and version of the application.

    The \[ServicePack\] section allows a network administrator to set the minimum required service pack level. The network administrator can use this section to author the text of an alert message displayed if the local operating system does not have the required service pack.

    The following is a sample Autorun.inf.

    ``` syntax
    [autorun] 
    OPEN=setup.EXE /AUTORUN /KEY:Software\Microsoft\Office\9.0\Common\General\InstallProductID
    ICON=setup.EXE,1
    shell\configure=&Configure
    shell\configure\command=setup.EXE
    shell\install=&Install
    shell\install\command=setup.EXE
    [OfficeFeatures]
    Feature1=ACCESSFiles
    Feature2=OfficeFiles
    Feature3=WORDFiles
    Feature4=EXCELFiles
    Feature5=PPTFiles
    [ProductInformation]
    DisplayName=Microsoft Office 9
    Version=9.0
    ProductCode={product guid}
    [ServicePack]
    MessageText="The operating system does not have a required service pack. Please download and install this from www.microsoft.com."
    SPLevel=3
    ```

2.  The Setup.exe application checks for the \_MsiPromptForCD mutex. Windows Installer creates this mutex when it prompts the user to insert the CD-ROM. The presence of the mutex indicates that Windows Installer is running an installation that has requested the Office 2000 CD-ROM. In this case, the Setup.exe application exits immediately and allows the Office 2000 installation to continue. If the mutex is absent, the Setup.exe application continues at step 3 where a registry key is evaluated to determine if Office 2000 is installed.
3.  The Setup.exe application checks the presence of the Office9 registry key:

    **HKCU/Software/Microsoft/Office/9.0/Common/General/InstallProductID**

    If this registry key does not exist, the Setup.exe application continues at step 6 where the operating system is checked to determine if it qualifies for the installation of Office 2000.

4.  If the Office 2000 registry key exists, the Setup.exe application checks the current installation state by calling [**MsiQueryProductState**](/windows/desktop/api/Msi/nf-msi-msiqueryproductstatea). A return state of InstallState\_Default indicates that Office 2000 is already installed and the Setup.exe application continues at step 5 where the Office 2000 is checked for run from source.

    If Office 2000 is not installed, the Setup.exe application continues at step 6 where the operating system is checked to determine if it qualifies for the installation of Office 2000.

5.  The Setup.exe application calls [**MsiQueryFeatureState**](/windows/desktop/api/Msi/nf-msi-msiqueryfeaturestatea) for each of the features in the **\[OfficeFeatures\]** section of the Autorun.inf file. If any of these features returns INSTALLSTATE\_SOURCE, this indicates that the feature is being run from source and the Setup.exe application exits immediately.

    If none of the features returns INSTALLSTATE\_SOURCE, the Setup.exe application launches the installer application, Msiexec.exe, and presents the Windows Installer maintenance mode before exiting.

6.  The Setup.exe application determines whether the operating system qualifies for an installation of Office 2000. Windows XP is required to install Office 2000. If the operating system requires a service pack update to qualify for Office 2000, the Setup.exe application displays the text specified in the Autorun.inf file. If the operating system does not qualify for Office 2000 or an upgrade of Office 2000, the Setup.exe application displays a message that prevents the user from continuing.

    If the operating system qualifies for Office 2000, the Setup.exe application continues at step 7, which determines whether Windows Installer is installed on the user's computer.

7.  If Windows Installer exists on the user's machine, the Setup.exe application launches the Msiexec.exe application and passes the Office 2000 .msi file to it.

    If Windows Installer is not installed on the local machine, the Setup.exe application continues at step 8, which determines whether the operating system qualifies to have Windows Installer installed.

8.  If the local computer is eligible to have Windows Installer installed, the Setup.exe application runs the correct version of the Instmsi.exe installer application for the platform. Setup.exe may pass the "/q" command line switch to suppress the user interface and prevent the user from changing any installation configuration options.
9.  The Setup.exe application loads the newly installed Msi.dll file and performs a call to the [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta) function to install the user's application.

## Setup.exe Command Line Parameters

The Setup.exe application enables administrators and users to pass command line options to the Msiexec.exe application. For more information, see [Command Line Options](command-line-options.md). The following table lists the command options that can be used with Setup.exe.



| Option                       | Usage                                                                                                                                        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /autorun                     | setup.exe /autorun                                                                                                                           | Runs the Autorun.inf described above.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| /a                           | setup.exe /a                                                                                                                                 | Initiates an administrative installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| /j                           | \[u\|m\]*Package*or <br/> \[u\|m\]*Package* /t *Transform List*<br/> or <br/> \[u\|m\]*Package* /g *LanguageID*<br/> | Advertises a product. This option ignores any property values entered on the command line. u   Advertise to the current user.<br/> m   Advertise to all users of machine.<br/> g   Language identifier<br/> t   Applies transform to advertised package.<br/>                                                                                                                                                                                                                        |
| /I                           | setup.exe /I Office9.msi /t ProgramMgmt.mst                                                                                                  | Specifies the .msi file that Setup.exe is to install. If the /I option is not included, Setup.exe uses the Office9.msi file.                                                                                                                                                                                                                                                                                                                                                                                 |
| /o<*property*=*value*> | setup.exe /o CDKEY=111111-1111                                                                                                               | Sets properties in the .msi file. Setup.exe passes these it to msiexec as written.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| /q                           | setup.exe /q                                                                                                                                 | Set the UI level the installation. /q   no UI (/qn   for msiexec.) /qb   basic UI<br/> /qr   reduced UI.<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| /m\#                         | setup.exe /m4                                                                                                                                | Supports multiple licenses in accordance with Select agreements. This property is used in by the License Verification custom action to write the LV certificate. The /m option must be followed by the number of unlocks allowed. The value specified by the /m option should be set as the "M" property in the Office9.msi file. If no value is specified, but the /m option is used with setup, the value of 0 should be set. The /m option is required to support Select customers using a CD or network. |
| /settings                    | setup.exe /settings mysettings.ini                                                                                                           | Enables administrators to specify an .ini file containing all of the customized settings to be passed during Office 2000 setup. See the description of the .ini file below.                                                                                                                                                                                                                                                                                                                                  |



 

## Using an .ini File

Creating an initialization file may be easier than creating a long command line. Using the /settings option, the Setup.exe application reads the specified .ini file and constructs a command line to pass to the Msiexec.exe application. Only properties supported on the command line are supported in the .ini file. If a property or value is found in both the .ini file and on the command line, the command line settings override the .ini file settings.

The format of the .ini file is:

\[msi\]

 

\[mst\]

 

\[options\]

 

\[Display\]

The \[msi\] section of the .ini file specifies the path to the installation package for the installation. This corresponds to the /I option on the command line.

The \[mst\] section of the .ini file specifies the path to transforms used with this installation. This corresponds to the /j option on the command line. Multiple transforms are each indicated on a different line, using MST1   MST(N). When parsed into the command line, the list in the .ini file is turned from left to right. Note that the number associated with the MST(N) title is present only to maintain unique identifiers and has no programmatic meaning.

The \[options\] section allows network administrators to set and override properties in the .msi or .mst files. Options set in the .ini file are added to the command line using the /o option. Each option in the option section must have a property name and a value.

The \[Display\] section is used to set the user interface level used during setup. This corresponds to the /q option on the command line. Valid values are   none, basic, reduced, and full.

Sample .ini file

\[MSI\]

 

MSI=\\\\sourceshare\\Office2000\\Office2000.msi

 

\[MST\]

 

MST1=\\\\sourceshare\\Office2000\\trns1.mst

 

MST2=\\\\sourceshare\\Office2000\\trns2.mst

 

\[Options\]

 

PUBLICPROPERTY=your value

\[Display\]

 

Display=None

 

