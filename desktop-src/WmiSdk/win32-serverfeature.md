---
Description: The Win32\_ServerFeature class represents the features installed on a computer running Windows Server.
ms.assetid: fe3bb95c-7f69-47b5-9c3d-771cdc3ed9ca
ms.tgt_platform: multiple
title: Win32_ServerFeature class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ServerFeature
- Win32_ServerFeature.ID
- Win32_ServerFeature.ParentID
- Win32_ServerFeature.Name
api_type: 
- DllExport
api_location: 
- ServerCompProv.dll
---

# Win32\_ServerFeature class

\[The **Win32\_ServerFeature** class is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [ServerManager Deploymentprovider Provider Classes](https://msdn.microsoft.com/library/hh872518).\]

The **Win32\_ServerFeature** class represents the features installed on a computer running Windows Server.

This class can be used by developers and administrators who need to automate the process of determining the features installed on a set of server computers. Instances of this class are not available on client computers.

## Syntax

``` syntax
[Deprecated("No value"), Dynamic, Provider("ServerFeatureProvider"), AMENDMENT]
class Win32_ServerFeature
{
  uint32 ID;
  uint32 ParentID;
  string Name;
};
```

## Members

The **Win32\_ServerFeature** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ServerFeature** class has these properties.

<dl> <dt>

**ID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Key**](key-qualifier.md), [**Not\_Null**](optional-qualifiers.md)
</dt> </dl>

Server feature ID. The following list shows the possible values of the ID property:



Value

Name

1

[Application Server](https://docs.microsoft.com/windows)

2

Web Server (IIS)

3

[Streaming Media Services](https://docs.microsoft.com/windows)

5

Fax Server

6

File and iSCSI Services<br/> [name change](https://docs.microsoft.com/windows)<br/>

7

Print and Document Services<br/> [name change](https://docs.microsoft.com/windows)<br/>

8

[Active Directory Federation Services](https://docs.microsoft.com/windows)

9

Active Directory Lightweight Directory Services

10

Active Directory Domain Services

11

[UDDI Services](https://docs.microsoft.com/windows)<br/>

12

[DHCP Server](https://docs.microsoft.com/windows)

13

[DNS Server](https://docs.microsoft.com/windows)

14

Network Policy and Access Services

16

Active Directory Certificate Services

17

Active Directory Rights Management Services

18

[Remote Desktop Services](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

19

Windows Deployment Services

20

Hyper-V

21

[Windows Server Update Services](https://docs.microsoft.com/windows)

33

[Failover Clustering](https://docs.microsoft.com/windows)

34

[Network Load Balancing](https://docs.microsoft.com/windows)

36

[.NET Framework 3.5.1 Features](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

37

[Windows System Resource Manager](https://docs.microsoft.com/windows)

38

Wireless LAN Service

39

[Windows Server Backup Features](https://docs.microsoft.com/windows)

40

WINS Server

41

Windows Process Activation Service

42

[Remote Assistance](https://docs.microsoft.com/windows)

43

Simple TCP/IP Services

44

[Telnet Client](https://docs.microsoft.com/windows)

45

[Telnet Server](https://docs.microsoft.com/windows)

46

[Subsystem For Unix-based Applications](https://docs.microsoft.com/windows)

47

RPC Over HTTP Proxy

48

SMTP Server

49

Message Queuing

51

[Windows Internal Database](https://docs.microsoft.com/windows)

52

[Storage Manager For SANs](https://docs.microsoft.com/windows)

53

LPR Port Monitor

55

[Internet Storage Name Server](https://docs.microsoft.com/windows)

57

[Multipath I/O](https://docs.microsoft.com/windows)

58

TFTP Client

59

[SNMP Services](https://docs.microsoft.com/windows)

60

[Removable Storage Manager](https://docs.microsoft.com/windows)

61

BitLocker Drive Encryption

62

[Services For Network File System](https://docs.microsoft.com/windows)

63

Internet Printing Client

64

[Peer Name Resolution Protocol](https://docs.microsoft.com/windows)

65

Connection Manager Administration Kit

66

[Windows PowerShell](https://docs.microsoft.com/windows)<br/>

67

[Remote Server Administration Tools](https://docs.microsoft.com/windows)

68

[Quality Windows Audio Video Experience](https://docs.microsoft.com/windows)

69

[Group Policy Management](https://docs.microsoft.com/windows)

71

[Indexing Service](https://docs.microsoft.com/windows)

72

[File Server Resource Manager (FSRM)](https://docs.microsoft.com/windows)

73

Remote Differential Compression

310

Ink and Handwriting Services<br/>

320

[Windows Server Migration Tools](https://docs.microsoft.com/windows)<br/>

321

[WinRM IIS Extension](https://docs.microsoft.com/windows)<br/>

324

[BranchCache](#branchcache)<br/>

334

[DirectAccess Management Console](https://docs.microsoft.com/windows)<br/>

335

[Background Intelligent Transfer Service (BITS)](https://docs.microsoft.com/windows)<br/>

338

[XPS Viewer](https://docs.microsoft.com/windows)<br/>

339

[Windows Biometric Framework](https://docs.microsoft.com/windows)<br/>

340

WoW64 Support<br/>

351

[Windows PowerShell Integrated Scripting Environment (ISE)](https://docs.microsoft.com/windows)<br/>

352

Windows TIFF IFilter<br/>

404

[Window Server Update Services](https://docs.microsoft.com/windows)

409

[IP Address Management (IPAM) Server](https://docs.microsoft.com/windows)

417

[Windows PowerShell](https://docs.microsoft.com/windows)

418

[.NET Framework 4.5](https://docs.microsoft.com/windows)

432

[Windows Search Service](https://docs.microsoft.com/windows)

438

[Client for NFS](https://docs.microsoft.com/windows)

441

[BitLocker Network Unlock](https://docs.microsoft.com/windows)

442

[Management OData IIS Extension](https://docs.microsoft.com/windows)

450

[.NET Framework 4.5 Advanced Services](https://docs.microsoft.com/windows)

466

[.NET Framework 4.5 Features](https://docs.microsoft.com/windows)

468

[Remote Access](https://docs.microsoft.com/windows)<br/>

477

[User Interfaces and Infrastructure](https://docs.microsoft.com/windows)

478

[Graphical Management Tools and Infrastructure](https://docs.microsoft.com/windows)

481

[File and Storage Services](https://docs.microsoft.com/windows)

485

[Windows Server Essentials Experience](https://docs.microsoft.com/windows)

488

[Direct Play](https://docs.microsoft.com/windows)

File Services - Role Services (6)

Value

Name

100

[Distributed File System](https://docs.microsoft.com/windows)

101

DFS Namespace

102

DFS Replication

103

[File Replication Service](https://docs.microsoft.com/windows)

104

[File Server Resource Manager (FSRM)](https://docs.microsoft.com/windows)

105

[Services For Network File System](https://docs.microsoft.com/windows)

106

[Single Instance Storage](https://docs.microsoft.com/windows)

107

[Windows Search Service](https://docs.microsoft.com/windows)

108

[Indexing Service](https://docs.microsoft.com/windows)

255

File Server

350

BranchCache for Network Files

431

[Server for NFS](https://docs.microsoft.com/windows)<br/>

434

[File Server VSS Agent Service](https://docs.microsoft.com/windows)<br/>

435

[iSCSI Target Server](https://docs.microsoft.com/windows)<br/>

436

[Data Deduplication](https://docs.microsoft.com/windows)<br/>

437

[iSCSI Target Storage Provider (VDS and VSS hardware providers)](https://docs.microsoft.com/windows)

486

[Work Folders](https://docs.microsoft.com/windows)

AD DS - Role Services (10)

Value

Name

110

[Active Directory Domain Controller](https://docs.microsoft.com/windows)

111

[Identity Management For Unix](https://docs.microsoft.com/windows)

112

[Server For Network Information Services](https://docs.microsoft.com/windows)

113

[Password Synchronization](https://docs.microsoft.com/windows)

294

[Remote Server Administration Tools](https://docs.microsoft.com/windows)

Streaming Media - Role Services (3)

Value

Name

120

[Windows Media Server](https://docs.microsoft.com/windows)

121

[Web-based Administration](https://docs.microsoft.com/windows)

122

[Logging Agent](https://docs.microsoft.com/windows)

ADFS - Role Services (8)

Value

Name

125

[Active Directory Federation Services](https://docs.microsoft.com/windows)

126

[Federation Service Policy](https://docs.microsoft.com/windows)

127

[AD FS Web Agents](https://docs.microsoft.com/windows)

128

[Claims-aware Agent](https://docs.microsoft.com/windows)

129

[Windows Token-based Agent](https://docs.microsoft.com/windows)

Remote Desktop Services - Role Services (18)

Value

Name

130

Remote Desktop Session Host<br/> [name change](https://docs.microsoft.com/windows)<br/>

131

[Remote Desktop Licensing](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

132

Remote Desktop Gateway<br/> [name change](https://docs.microsoft.com/windows)<br/>

133

Remote Desktop Connection Broker<br/> [name change](https://docs.microsoft.com/windows)<br/>

134

Remote Desktop Web Access<br/> [name change](https://docs.microsoft.com/windows)<br/>

322

Remote Desktop Virtualization Host<br/>

Remote Desktop Virtualization Host - Role Services (322)

Value

Name

325

[Core Services](https://docs.microsoft.com/windows)<br/>

327

[Remote Desktop Virtual Graphics](https://docs.microsoft.com/windows)<br/>

Print and Document Services - Role Services (7)

Value

Name

135

Print Server

136

Internet Printing

137

LPD Print Service

328

[Distributed Scan Server](https://docs.microsoft.com/windows)<br/>

Web Server (IIS) - Role Services (2)

Value

Name

140

Web Server

141

Common HTTP Features

142

Static Content

143

Default Document

144

Directory Browse

145

HTTP Errors

146

HTTP Redirection

147

Application Development

148

ASP.NET

149

.NET Extensibility

150

ASP

151

CGI

152

ISAPI Extensions

153

ISAPI Filters

154

Server Side Includes

155

Health And Diagnostics

156

HTTP Logging

157

Logging Tools

158

Request Monitor

159

Tracing

160

Custom Logging

161

ODBC Logging

162

Security

163

Basic Authentication

164

Windows Authentication

165

Digest Authentication

166

Client Certificate Mapping Authentication

167

IIS Client Certificate Mapping Authentication

168

URL Authorization

169

Request Filtering

170

IP And Domain Restrictions

171

Performance

172

Static Content Compression

173

Dynamic Content Compression

174

Management Tools

175

IIS Management Console

176

IIS Management Scripts And Tools

177

Management Service

178

IIS 6 Management Compatibility

179

IIS 6 Metabase Compatibility

180

IIS 6 WMI Compatibility

181

IIS 6 Scripting Tools

182

IIS 6 Management Console

183

FTP Publishing Service<br/>

184

FTP Server

185

FTP Management Console<br/>

314

WebDAV Publishing

316

FTP Service<br/>

317

FTP Extensibility<br/>

336

IIS Hostable Web Core<br/>

413

[ASP.NET 4.5](https://docs.microsoft.com/windows)

414

[.NET Extensibility 4.5](https://docs.microsoft.com/windows)

445

[appialization](https://docs.microsoft.com/windows)

446

[Centralized SSL Certificate Support](https://docs.microsoft.com/windows)

447

[WebSocket Protocol](https://docs.microsoft.com/windows)

Message Queuing - Features (49)

Value

Name

190

Message Queuing Services

191

Message Queuing Server

192

Directory Service Integration

193

Message Queuing Triggers

194

HTTP Support

195

Routing Service

196

[Windows 2000 Client Support](https://docs.microsoft.com/windows)<br/>

197

Message Queuing DCOM Proxy

228

Multicasting Support

Active Directory Certificate Services - Role Services (16)

Value

Name

200

Certification Authority

201

Certification Authority Web Enrollment

202

Online Responder

204

Network Device Enrollment Service

318

[Certificate Enrollment Web Service](https://docs.microsoft.com/windows)<br/>

319

[Certificate Enrollment Policy Web Service](https://docs.microsoft.com/windows)<br/>

Network Policy and Access Services - Role Services (14)

Value

Name

205

[Network Policy Server](https://docs.microsoft.com/windows)

206

[VPN](#vpn)

207

[Remote Access Services](https://docs.microsoft.com/windows)

208

[Routing](#routing)

210

[Health Registration Authority](https://docs.microsoft.com/windows)

250

[Host Credential Authorization Protocol](https://docs.microsoft.com/windows)

UDDI Services - Role Services (11)

Value

Name

215

[UDDI Services Web Application](https://docs.microsoft.com/windows)<br/>

216

[UDDI Services Database](https://docs.microsoft.com/windows)<br/>

Windows Process Activation Service - Role Services (41)

Value

Name

217

Configuration API

218

.NET Environment

219

Process Model

.NET Framework 3.5.1 - Features (36)

Value

Name

220

.NET Framework 3.5.1<br/> [name change](https://docs.microsoft.com/windows)<br/>

221

WCF Activation

222

HTTP Activation

223

Non-HTTP Activation

227

XPS Viewer<br/>

SNMP Services - Features (59)

Value

Name

224

[SNMP Service](https://docs.microsoft.com/windows)

225

[SNMP WMI Provider](https://docs.microsoft.com/windows)

Application Services - Role Services

Value

Name

230

[.NET Framework 3.5.1](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

231

[Web Server (IIS) Support](https://docs.microsoft.com/windows)

232

[COM+ Network Access](https://docs.microsoft.com/windows)

233

[TCP Port Sharing](https://docs.microsoft.com/windows)

234

[Windows Process Activation Service Support](https://docs.microsoft.com/windows)

235

[HTTP Activation](https://docs.microsoft.com/windows)

236

[Message Queuing Activation](https://docs.microsoft.com/windows)

237

[TCP Activation](https://docs.microsoft.com/windows)

238

[Named Pipes Activation](https://docs.microsoft.com/windows)

239

[Distributed Transactions](https://docs.microsoft.com/windows)

240

[Incoming Remote Transactions](https://docs.microsoft.com/windows)

241

[Outgoing Remote Transactions](https://docs.microsoft.com/windows)

242

[WS-Automatic Transactions](https://docs.microsoft.com/windows)

353

[Application Server Extensions for .NET 4.0](https://docs.microsoft.com/windows)<br/>

Windows Deployment Services - Role (19)

Value

Name

251

Deployment Server

252

Transport Server

Active Directory Rights Management Services - Role Services (17)

Value

Name

253

Active Directory Rights Management Server

254

Identity Federation Support

Remote Server Administration Tools (67)

Value

Name

256

[Role Administration Tools](https://docs.microsoft.com/windows)

257

[AD DS Tools](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

258

[AD LDS Snap-Ins and Command-Line Tools](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

259

Active Directory Certificate Services Tools

260

[Network Policy and Access Services](https://docs.microsoft.com/windows)

261

Print and Document Services Tools<br/> [name change](https://docs.microsoft.com/windows)<br/>

262

[Active Directory Rights Management Services](https://docs.microsoft.com/windows)

263

[Remote Desktop Services Tools](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

264

Windows Deployment Services Tools

265

[Feature Administration Tools](https://docs.microsoft.com/windows)

266

BitLocker Drive Encryption Tools

267

BITS Server Extensions Tools

268

[Failover Clustering Tools](https://docs.microsoft.com/windows)

269

Network Load Balancing Tools

270

SMTP Server Tools

273

[DNS Server Tools](https://docs.microsoft.com/windows)

277

File Services Tools

278

Distributed File System Tools

279

File Server Resource Manager Tools

280

[Services For Network File System Tools](https://docs.microsoft.com/windows)

281

Web Server (IIS) Tools

284

[Remote Desktop Session Host Tools](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

285

Remote Desktop Gateway Tools<br/> [name change](https://docs.microsoft.com/windows)<br/>

286

Remote Desktop Licensing Tools<br/> [name change](https://docs.microsoft.com/windows)<br/>

288

Fax Server Tools

290

WINS Server Tools

291

[UDDI Services Tools](https://docs.microsoft.com/windows)<br/>

292

Certification Authority Tools

293

Online Responder Tools

297

[Server for NIS Tools](https://docs.microsoft.com/windows)

299

[AD DS Snap-Ins and Command-Line Tools](https://docs.microsoft.com/windows)<br/> [name change](https://docs.microsoft.com/windows)<br/>

300

[Active Directory Administrative Center](https://docs.microsoft.com/windows)

301

Hyper-V Tools

323

[BitLocker Recovery Password Viewer](https://docs.microsoft.com/windows)<br/>

326

[BitLocker Drive Encryption Administration Utilities](https://docs.microsoft.com/windows)<br/>

329

[AD DS and AD LDS Tools](https://docs.microsoft.com/windows)<br/>

330

Active Directory Administrative Center<br/>

331

[Active Directory module for Windows PowerShell](https://docs.microsoft.com/windows)<br/>

337

[Remote Desktop Connection Broker Tools](https://docs.microsoft.com/windows)<br/>

410

[IP Address Management (IPAM) Client](https://docs.microsoft.com/windows)

450

[Hyper-V Module for Windows PowerShell](https://docs.microsoft.com/windows)

462

[Active Directory Rights Management Services Tools](https://docs.microsoft.com/windows)

465

[Share and Storage Management Tool](https://docs.microsoft.com/windows)

471

[Remote Access Management Tools](https://docs.microsoft.com/windows)

472

[Remote Access module for Windows PowerShell](https://docs.microsoft.com/windows)

473

[Remote Access GUI and Command-Line Tools](https://docs.microsoft.com/windows)

474

[Windows Server Update Services Tools](https://docs.microsoft.com/windows)

476

[Remote Desktop Licensing Diagnoser Tools](https://docs.microsoft.com/windows)

479

[SNMP Tools](https://docs.microsoft.com/windows)

480

[Volume Activation Tools](https://docs.microsoft.com/windows)

Windows Server Backup - Features (39)

Value

Name

296

[Windows Server Backup](https://docs.microsoft.com/windows)

297

[Command Line Tools](https://docs.microsoft.com/windows)

Ink and Handwriting Services - Features (310)

Value

Name

311

[Ink Support](https://docs.microsoft.com/windows)<br/>

312

[Handwriting Recognition](https://docs.microsoft.com/windows)<br/>

Background Intelligent Transfer Service (BITS) - Features (335)

Value

Name

54

IIS Server Extension

332

[Compact Server](https://docs.microsoft.com/windows)<br/>

Wow64 Support - Features (340)

Value

Name

341

[WoW64](#wow64)<br/>

342

[WoW64 for .NET Framework 2.0 and Windows PowerShell](https://docs.microsoft.com/windows)<br/>

343

[WoW64 for .NET Framework 2.0](https://docs.microsoft.com/windows)<br/>

344

[WoW64 for PowerShell](https://docs.microsoft.com/windows)<br/>

345

[WoW64 for .NET Framework 3.0 and 3.5](https://docs.microsoft.com/windows)<br/>

346

[WoW64 for Print Services](https://docs.microsoft.com/windows)<br/>

347

[WoW64 for Failover Clustering](https://docs.microsoft.com/windows)<br/>

348

[WoW64 for Input Method Editor](https://docs.microsoft.com/windows)<br/>

349

[WoW64 for Subsystem for UNIX-based Applications](https://docs.microsoft.com/windows)<br/>

User Interfaces and Infrastructure - Role Services (447)

Value

Name

35

[Desktop Experience](https://docs.microsoft.com/windows)

99

[Server Graphical Shell](https://docs.microsoft.com/windows)

Window Server Update Services - Features (404)

Value

Name

405

[API and PowerShell cmdlets](https://docs.microsoft.com/windows)

406

[SQL Server Connectivity](https://docs.microsoft.com/windows)

407

[WSUS Services](https://docs.microsoft.com/windows)

408

[User Interface Management Console](https://docs.microsoft.com/windows)

449

[WID Connectivity](https://docs.microsoft.com/windows)

Windows PowerShell - Features (417)

Value

Name

411

[Windows PowerShell 2.0 Engine](https://docs.microsoft.com/windows)

412

[Windows PowerShell 3.0](https://docs.microsoft.com/windows)

448

[Windows PowerShell Web Access](https://docs.microsoft.com/windows)

1000

[Windows PowerShell Desired State Configuration Service](https://docs.microsoft.com/windows)

.NET Framework 4.5 - Features (418)

Value

Name

419

[.NET Framework 4.5 Extended](https://docs.microsoft.com/windows)

420

[WCF Services](https://docs.microsoft.com/windows)

421

[HTTP Activation](https://docs.microsoft.com/windows)

422

[Message Queuing (MSMQ) Activation](https://docs.microsoft.com/windows)

423

[Named Pipe Activation](https://docs.microsoft.com/windows)

424

[TCP Activation](https://docs.microsoft.com/windows)

425

[TCP Port Sharing](https://docs.microsoft.com/windows)

429

[ASP.NET 4.5](https://docs.microsoft.com/windows)

Remote Access - Role (468)

Value

Name

469

[DirectAccess and VPN (RAS)](https://docs.microsoft.com/windows)

470

[Routing](#routing)

File and Storage Services - Role (481)

Value

Name

482

[Storage Services](https://docs.microsoft.com/windows)

484

[Failover Cluster Management Tools](https://docs.microsoft.com/windows)



 

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Display name of the server feature, such as "File Server", "Print Server", or "Desktop Experience".

</dd> <dt>

**ParentID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

ID number of the parent server feature. This property is 0 if the feature represented by the current instance of the class does not have a parent feature.

</dd> </dl>

## Remarks

Read the [Windows Server 2008 Server Manager Technical Overview](https://go.microsoft.com/fwlink/p/?linkid=109936) to learn about server features.

Enterprises that do not use management software that reports server features, such as System Center Operations Manager with management packs installed, can get that information by querying the **Win32\_ServerFeature** class.

You can use the remoting features of WMI or WinRM to get server feature information from remote servers. For more information about remote WMI DCOM connections, see [Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md). For more information about WinRM, see Windows Remote Management.

Windows Server 2012: **Win32\_ServerFeature** has been deprecated. To access windows server feature information programmatically, you can use the [Server Manager Cmdlets](https://TechNet.Microsoft.Com/library/ee662311.aspx).

### Windows Server 2012 R2

<dl> <dt>

<span id="Application_Server"></span><span id="application_server"></span><span id="APPLICATION_SERVER"></span>Application Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Streaming_Media_Services"></span><span id="streaming_media_services"></span><span id="STREAMING_MEDIA_SERVICES"></span>Streaming Media Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Active_Directory_Federation_Services"></span><span id="active_directory_federation_services"></span><span id="ACTIVE_DIRECTORY_FEDERATION_SERVICES"></span>Active Directory Federation Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="DHCP_Server"></span><span id="dhcp_server"></span><span id="DHCP_SERVER"></span>DHCP Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="DNS_Server"></span><span id="dns_server"></span><span id="DNS_SERVER"></span>DNS Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Desktop_Services"></span><span id="remote_desktop_services"></span><span id="REMOTE_DESKTOP_SERVICES"></span>Remote Desktop Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Server_Update_Services"></span><span id="windows_server_update_services"></span><span id="WINDOWS_SERVER_UPDATE_SERVICES"></span>Windows Server Update Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Failover_Clustering"></span><span id="failover_clustering"></span><span id="FAILOVER_CLUSTERING"></span>Failover Clustering
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Network_Load_Balancing"></span><span id="network_load_balancing"></span><span id="NETWORK_LOAD_BALANCING"></span>Network Load Balancing
</dt> <dd>

No longer supported

</dd> <dt>

<span id=".NET_Framework_3.5.1_Features"></span><span id=".net_framework_3.5.1_features"></span><span id=".NET_FRAMEWORK_3.5.1_FEATURES"></span>.NET Framework 3.5.1 Features
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_System_Resource_Manager"></span><span id="windows_system_resource_manager"></span><span id="WINDOWS_SYSTEM_RESOURCE_MANAGER"></span>Windows System Resource Manager
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Server_Backup_Features"></span><span id="windows_server_backup_features"></span><span id="WINDOWS_SERVER_BACKUP_FEATURES"></span>Windows Server Backup Features
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Assistance"></span><span id="remote_assistance"></span><span id="REMOTE_ASSISTANCE"></span>Remote Assistance
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Telnet_Client"></span><span id="telnet_client"></span><span id="TELNET_CLIENT"></span>Telnet Client
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Telnet_Server"></span><span id="telnet_server"></span><span id="TELNET_SERVER"></span>Telnet Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Subsystem_For_Unix-based_Applications"></span><span id="subsystem_for_unix-based_applications"></span><span id="SUBSYSTEM_FOR_UNIX-BASED_APPLICATIONS"></span>Subsystem For Unix-based Applications
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Internal_Database"></span><span id="windows_internal_database"></span><span id="WINDOWS_INTERNAL_DATABASE"></span>Windows Internal Database
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Storage_Manager_For_SANs"></span><span id="storage_manager_for_sans"></span><span id="STORAGE_MANAGER_FOR_SANS"></span>Storage Manager For SANs
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Internet_Storage_Name_Server"></span><span id="internet_storage_name_server"></span><span id="INTERNET_STORAGE_NAME_SERVER"></span>Internet Storage Name Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Multipath_I_O"></span><span id="multipath_i_o"></span><span id="MULTIPATH_I_O"></span>Multipath I/O
</dt> <dd>

No longer supported

</dd> <dt>

<span id="SNMP_Services"></span><span id="snmp_services"></span><span id="SNMP_SERVICES"></span>SNMP Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Services_For_Network_File_System"></span><span id="services_for_network_file_system"></span><span id="SERVICES_FOR_NETWORK_FILE_SYSTEM"></span>Services For Network File System
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Peer_Name_Resolution_Protocol"></span><span id="peer_name_resolution_protocol"></span><span id="PEER_NAME_RESOLUTION_PROTOCOL"></span>Peer Name Resolution Protocol
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Server_Administration_Tools"></span><span id="remote_server_administration_tools"></span><span id="REMOTE_SERVER_ADMINISTRATION_TOOLS"></span>Remote Server Administration Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Quality_Windows_Audio_Video_Experience"></span><span id="quality_windows_audio_video_experience"></span><span id="QUALITY_WINDOWS_AUDIO_VIDEO_EXPERIENCE"></span>Quality Windows Audio Video Experience
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Group_Policy_Management"></span><span id="group_policy_management"></span><span id="GROUP_POLICY_MANAGEMENT"></span>Group Policy Management
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Indexing_Service"></span><span id="indexing_service"></span><span id="INDEXING_SERVICE"></span>Indexing Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="File_Server_Resource_Manager__FSRM_"></span><span id="file_server_resource_manager__fsrm_"></span><span id="FILE_SERVER_RESOURCE_MANAGER__FSRM_"></span>File Server Resource Manager (FSRM)
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Server_Migration_Tools"></span><span id="windows_server_migration_tools"></span><span id="WINDOWS_SERVER_MIGRATION_TOOLS"></span>Windows Server Migration Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="BranchCache"></span><span id="branchcache"></span><span id="BRANCHCACHE"></span>BranchCache
</dt> <dd>

No longer supported

</dd> <dt>

<span id="DirectAccess_Management_Console"></span><span id="directaccess_management_console"></span><span id="DIRECTACCESS_MANAGEMENT_CONSOLE"></span>DirectAccess Management Console
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Background_Intelligent_Transfer_Service__BITS_"></span><span id="background_intelligent_transfer_service__bits_"></span><span id="BACKGROUND_INTELLIGENT_TRANSFER_SERVICE__BITS_"></span>Background Intelligent Transfer Service (BITS)
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_Support"></span><span id="wow64_support"></span><span id="WOW64_SUPPORT"></span>WoW64 Support
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Window_Server_Update_Services"></span><span id="window_server_update_services"></span><span id="WINDOW_SERVER_UPDATE_SERVICES"></span>Window Server Update Services
</dt> <dd>

Added

</dd> <dt>

<span id="IP_Address_Management__IPAM__Server"></span><span id="ip_address_management__ipam__server"></span><span id="IP_ADDRESS_MANAGEMENT__IPAM__SERVER"></span>IP Address Management (IPAM) Server
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_PowerShell"></span><span id="windows_powershell"></span><span id="WINDOWS_POWERSHELL"></span>Windows PowerShell
</dt> <dd>

Added

</dd> <dt>

<span id=".NET_Framework_4.5"></span><span id=".net_framework_4.5"></span><span id=".NET_FRAMEWORK_4.5"></span>.NET Framework 4.5
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_Search_Service"></span><span id="windows_search_service"></span><span id="WINDOWS_SEARCH_SERVICE"></span>Windows Search Service
</dt> <dd>

Added

</dd> <dt>

<span id="Client_for_NFS"></span><span id="client_for_nfs"></span><span id="CLIENT_FOR_NFS"></span>Client for NFS
</dt> <dd>

Added

</dd> <dt>

<span id="BitLocker_Network_Unlock"></span><span id="bitlocker_network_unlock"></span><span id="BITLOCKER_NETWORK_UNLOCK"></span>BitLocker Network Unlock
</dt> <dd>

Added

</dd> <dt>

<span id="Management_OData_IIS_Extension"></span><span id="management_odata_iis_extension"></span><span id="MANAGEMENT_ODATA_IIS_EXTENSION"></span>Management OData IIS Extension
</dt> <dd>

Added

</dd> <dt>

<span id=".NET_Framework_4.5_Advanced_Services"></span><span id=".net_framework_4.5_advanced_services"></span><span id=".NET_FRAMEWORK_4.5_ADVANCED_SERVICES"></span>.NET Framework 4.5 Advanced Services
</dt> <dd>

Added

</dd> <dt>

<span id=".NET_Framework_4.5_Features"></span><span id=".net_framework_4.5_features"></span><span id=".NET_FRAMEWORK_4.5_FEATURES"></span>.NET Framework 4.5 Features
</dt> <dd>

Added

</dd> <dt>

<span id="User_Interfaces_and_Infrastructure"></span><span id="user_interfaces_and_infrastructure"></span><span id="USER_INTERFACES_AND_INFRASTRUCTURE"></span>User Interfaces and Infrastructure
</dt> <dd>

Added

</dd> <dt>

<span id="Graphical_Management_Tools_and_Infrastructure"></span><span id="graphical_management_tools_and_infrastructure"></span><span id="GRAPHICAL_MANAGEMENT_TOOLS_AND_INFRASTRUCTURE"></span>Graphical Management Tools and Infrastructure
</dt> <dd>

Added

</dd> <dt>

<span id="File_and_Storage_Services"></span><span id="file_and_storage_services"></span><span id="FILE_AND_STORAGE_SERVICES"></span>File and Storage Services
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_Server_Essentials_Experience"></span><span id="windows_server_essentials_experience"></span><span id="WINDOWS_SERVER_ESSENTIALS_EXPERIENCE"></span>Windows Server Essentials Experience
</dt> <dd>

Added

</dd> <dt>

<span id="Direct_Play"></span><span id="direct_play"></span><span id="DIRECT_PLAY"></span>Direct Play
</dt> <dd>

Added

</dd> <dt>

<span id="Distributed_File_System"></span><span id="distributed_file_system"></span><span id="DISTRIBUTED_FILE_SYSTEM"></span>Distributed File System
</dt> <dd>

No longer supported

</dd> <dt>

<span id="File_Server_Resource_Manager"></span><span id="file_server_resource_manager"></span><span id="FILE_SERVER_RESOURCE_MANAGER"></span>File Server Resource Manager
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Services_For_Network_File_System"></span><span id="services_for_network_file_system"></span><span id="SERVICES_FOR_NETWORK_FILE_SYSTEM"></span>Services For Network File System
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Single_Instance_Storage"></span><span id="single_instance_storage"></span><span id="SINGLE_INSTANCE_STORAGE"></span>Single Instance Storage
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Search_Service"></span><span id="windows_search_service"></span><span id="WINDOWS_SEARCH_SERVICE"></span>Windows Search Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Indexing_Service"></span><span id="indexing_service"></span><span id="INDEXING_SERVICE"></span>Indexing Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="iSCSI_Target_Storage_Provider__VDS_and_VSS_hardware_providers_"></span><span id="iscsi_target_storage_provider__vds_and_vss_hardware_providers_"></span><span id="ISCSI_TARGET_STORAGE_PROVIDER__VDS_AND_VSS_HARDWARE_PROVIDERS_"></span>iSCSI Target Storage Provider (VDS and VSS hardware providers)
</dt> <dd>

Added

</dd> <dt>

<span id="Work_Folders"></span><span id="work_folders"></span><span id="WORK_FOLDERS"></span>Work Folders
</dt> <dd>

Added

</dd> <dt>

<span id="Active_Directory_Domain_Controller"></span><span id="active_directory_domain_controller"></span><span id="ACTIVE_DIRECTORY_DOMAIN_CONTROLLER"></span>Active Directory Domain Controller
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Identity_Management_For_Unix"></span><span id="identity_management_for_unix"></span><span id="IDENTITY_MANAGEMENT_FOR_UNIX"></span>Identity Management For Unix
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Server_For_Network_Information_Services"></span><span id="server_for_network_information_services"></span><span id="SERVER_FOR_NETWORK_INFORMATION_SERVICES"></span>Server For Network Information Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Password_Synchronization"></span><span id="password_synchronization"></span><span id="PASSWORD_SYNCHRONIZATION"></span>Password Synchronization
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Administration_Tools"></span><span id="administration_tools"></span><span id="ADMINISTRATION_TOOLS"></span>Administration Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Media_Server"></span><span id="windows_media_server"></span><span id="WINDOWS_MEDIA_SERVER"></span>Windows Media Server
</dt> <dd>

No longer supported.

</dd> <dt>

<span id="Web-based_Administration"></span><span id="web-based_administration"></span><span id="WEB-BASED_ADMINISTRATION"></span>Web-based Administration
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Logging_Agent"></span><span id="logging_agent"></span><span id="LOGGING_AGENT"></span>Logging Agent
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Federation_Service"></span><span id="federation_service"></span><span id="FEDERATION_SERVICE"></span>Federation Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Federation_Service_Policy"></span><span id="federation_service_policy"></span><span id="FEDERATION_SERVICE_POLICY"></span>Federation Service Policy
</dt> <dd>

No longer supported

</dd> <dt>

<span id="AD_FS_Web_Agents"></span><span id="ad_fs_web_agents"></span><span id="AD_FS_WEB_AGENTS"></span>AD FS Web Agents
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Token-based_Agent"></span><span id="windows_token-based_agent"></span><span id="WINDOWS_TOKEN-BASED_AGENT"></span>Windows Token-based Agent
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Desktop_Licensing"></span><span id="remote_desktop_licensing"></span><span id="REMOTE_DESKTOP_LICENSING"></span>Remote Desktop Licensing
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Network_Policy_Server"></span><span id="network_policy_server"></span><span id="NETWORK_POLICY_SERVER"></span>Network Policy Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="VPN"></span><span id="vpn"></span>VPN
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Access_Services"></span><span id="remote_access_services"></span><span id="REMOTE_ACCESS_SERVICES"></span>Remote Access Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Routing"></span><span id="routing"></span><span id="ROUTING"></span>Routing
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Health_Registration_Authority"></span><span id="health_registration_authority"></span><span id="HEALTH_REGISTRATION_AUTHORITY"></span>Health Registration Authority
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Host_Credential_Authorization_Protocol"></span><span id="host_credential_authorization_protocol"></span><span id="HOST_CREDENTIAL_AUTHORIZATION_PROTOCOL"></span>Host Credential Authorization Protocol
</dt> <dd>

No longer supported

</dd> <dt>

<span id=".NET_Framework_3.5.1"></span><span id=".net_framework_3.5.1"></span><span id=".NET_FRAMEWORK_3.5.1"></span>.NET Framework 3.5.1
</dt> <dd>

No longer supported

</dd> <dt>

<span id="XPS_Viewer"></span><span id="xps_viewer"></span><span id="XPS_VIEWER"></span>XPS Viewer
</dt> <dd>

No longer supported

</dd> <dt>

<span id="SNMP_Service"></span><span id="snmp_service"></span><span id="SNMP_SERVICE"></span>SNMP Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="SNMP_WMI_Provider"></span><span id="snmp_wmi_provider"></span><span id="SNMP_WMI_PROVIDER"></span>SNMP WMI Provider
</dt> <dd>

No longer supported

</dd> <dt>

<span id=".NET_Framework_3.5.1"></span><span id=".net_framework_3.5.1"></span><span id=".NET_FRAMEWORK_3.5.1"></span>.NET Framework 3.5.1
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Web_Server__IIS__Support"></span><span id="web_server__iis__support"></span><span id="WEB_SERVER__IIS__SUPPORT"></span>Web Server (IIS) Support
</dt> <dd>

No longer supported

</dd> <dt>

<span id="COM__Network_Access"></span><span id="com__network_access"></span><span id="COM__NETWORK_ACCESS"></span>COM+ Network Access
</dt> <dd>

No longer supported

</dd> <dt>

<span id="TCP_Port_Sharing"></span><span id="tcp_port_sharing"></span><span id="TCP_PORT_SHARING"></span>TCP Port Sharing
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_Process_Activation_Service_Support"></span><span id="windows_process_activation_service_support"></span><span id="WINDOWS_PROCESS_ACTIVATION_SERVICE_SUPPORT"></span>Windows Process Activation Service Support
</dt> <dd>

No longer supported

</dd> <dt>

<span id="HTTP_Activation"></span><span id="http_activation"></span><span id="HTTP_ACTIVATION"></span>HTTP Activation
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Message_Queuing_Activation"></span><span id="message_queuing_activation"></span><span id="MESSAGE_QUEUING_ACTIVATION"></span>Message Queuing Activation
</dt> <dd>

No longer supported

</dd> <dt>

<span id="TCP_Activation"></span><span id="tcp_activation"></span><span id="TCP_ACTIVATION"></span>TCP Activation
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Named_Pipes_Activation"></span><span id="named_pipes_activation"></span><span id="NAMED_PIPES_ACTIVATION"></span>Named Pipes Activation
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Distributed_Transactions"></span><span id="distributed_transactions"></span><span id="DISTRIBUTED_TRANSACTIONS"></span>Distributed Transactions
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Incoming_Remote_Transactions"></span><span id="incoming_remote_transactions"></span><span id="INCOMING_REMOTE_TRANSACTIONS"></span>Incoming Remote Transactions
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Outgoing_Remote_Transactions"></span><span id="outgoing_remote_transactions"></span><span id="OUTGOING_REMOTE_TRANSACTIONS"></span>Outgoing Remote Transactions
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WS-Automatic_Transactions"></span><span id="ws-automatic_transactions"></span><span id="WS-AUTOMATIC_TRANSACTIONS"></span>WS-Automatic Transactions
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Application_Server_Extensions_for_.NET_4.0"></span><span id="application_server_extensions_for_.net_4.0"></span><span id="APPLICATION_SERVER_EXTENSIONS_FOR_.NET_4.0"></span>Application Server Extensions for .NET 4.0
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Role_Administration_Tools"></span><span id="role_administration_tools"></span><span id="ROLE_ADMINISTRATION_TOOLS"></span>Role Administration Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="AD_DS_Tools"></span><span id="ad_ds_tools"></span><span id="AD_DS_TOOLS"></span>AD DS Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="AD_LDS_Snap-Ins_and_Command-Line_Tools"></span><span id="ad_lds_snap-ins_and_command-line_tools"></span><span id="AD_LDS_SNAP-INS_AND_COMMAND-LINE_TOOLS"></span>AD LDS Snap-Ins and Command-Line Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Network_Policy_and_Access_Services"></span><span id="network_policy_and_access_services"></span><span id="NETWORK_POLICY_AND_ACCESS_SERVICES"></span>Network Policy and Access Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Active_Directory_Rights_Management_Services"></span><span id="active_directory_rights_management_services"></span><span id="ACTIVE_DIRECTORY_RIGHTS_MANAGEMENT_SERVICES"></span>Active Directory Rights Management Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Desktop_Services_Tools"></span><span id="remote_desktop_services_tools"></span><span id="REMOTE_DESKTOP_SERVICES_TOOLS"></span>Remote Desktop Services Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Feature_Administration_Tools"></span><span id="feature_administration_tools"></span><span id="FEATURE_ADMINISTRATION_TOOLS"></span>Feature Administration Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Failover_Clustering_Tools"></span><span id="failover_clustering_tools"></span><span id="FAILOVER_CLUSTERING_TOOLS"></span>Failover Clustering Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="DNS_Server_Tools"></span><span id="dns_server_tools"></span><span id="DNS_SERVER_TOOLS"></span>DNS Server Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Services_For_Network_File_System_Tools"></span><span id="services_for_network_file_system_tools"></span><span id="SERVICES_FOR_NETWORK_FILE_SYSTEM_TOOLS"></span>Services For Network File System Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Web_Server__IIS__Tools"></span><span id="web_server__iis__tools"></span><span id="WEB_SERVER__IIS__TOOLS"></span>Web Server (IIS) Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Server_for_NIS_Tools"></span><span id="server_for_nis_tools"></span><span id="SERVER_FOR_NIS_TOOLS"></span>Server for NIS Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="AD_DS_Snap-Ins_and_Command-Line_Tools"></span><span id="ad_ds_snap-ins_and_command-line_tools"></span><span id="AD_DS_SNAP-INS_AND_COMMAND-LINE_TOOLS"></span>AD DS Snap-Ins and Command-Line Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="AD_DS_and_AD_LDS_Tools"></span><span id="ad_ds_and_ad_lds_tools"></span><span id="AD_DS_AND_AD_LDS_TOOLS"></span>AD DS and AD LDS Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Desktop_Connection_Broker_Tools"></span><span id="remote_desktop_connection_broker_tools"></span><span id="REMOTE_DESKTOP_CONNECTION_BROKER_TOOLS"></span>Remote Desktop Connection Broker Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="IP_Address_Management__IPAM__Client"></span><span id="ip_address_management__ipam__client"></span><span id="IP_ADDRESS_MANAGEMENT__IPAM__CLIENT"></span>IP Address Management (IPAM) Client
</dt> <dd>

Added

</dd> <dt>

<span id="Hyper-V_Module_for_Windows_PowerShell"></span><span id="hyper-v_module_for_windows_powershell"></span><span id="HYPER-V_MODULE_FOR_WINDOWS_POWERSHELL"></span>Hyper-V Module for Windows PowerShell
</dt> <dd></dd> <dt>

<span id="Active_Directory_Rights_Management_Services_Tool"></span><span id="active_directory_rights_management_services_tool"></span><span id="ACTIVE_DIRECTORY_RIGHTS_MANAGEMENT_SERVICES_TOOL"></span>Active Directory Rights Management Services Tool
</dt> <dd>

Added

</dd> <dt>

<span id="Share_and_Storage_Management_Tool"></span><span id="share_and_storage_management_tool"></span><span id="SHARE_AND_STORAGE_MANAGEMENT_TOOL"></span>Share and Storage Management Tool
</dt> <dd>

Added

</dd> <dt>

<span id="Remote_Access_Management_Tools"></span><span id="remote_access_management_tools"></span><span id="REMOTE_ACCESS_MANAGEMENT_TOOLS"></span>Remote Access Management Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Remote_Access_module_for_Windows_PowerShell"></span><span id="remote_access_module_for_windows_powershell"></span><span id="REMOTE_ACCESS_MODULE_FOR_WINDOWS_POWERSHELL"></span>Remote Access module for Windows PowerShell
</dt> <dd>

Added

</dd> <dt>

<span id="Remote_Access_GUI_and_Command-Line_Tools"></span><span id="remote_access_gui_and_command-line_tools"></span><span id="REMOTE_ACCESS_GUI_AND_COMMAND-LINE_TOOLS"></span>Remote Access GUI and Command-Line Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_Server_Update_Services_Tools"></span><span id="windows_server_update_services_tools"></span><span id="WINDOWS_SERVER_UPDATE_SERVICES_TOOLS"></span>Windows Server Update Services Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Remote_Desktop_Licensing_Diagnoser_Tools"></span><span id="remote_desktop_licensing_diagnoser_tools"></span><span id="REMOTE_DESKTOP_LICENSING_DIAGNOSER_TOOLS"></span>Remote Desktop Licensing Diagnoser Tools
</dt> <dd>

Added

</dd> <dt>

<span id="SNMP_Tools"></span><span id="snmp_tools"></span><span id="SNMP_TOOLS"></span>SNMP Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Volume_Activation_Tools"></span><span id="volume_activation_tools"></span><span id="VOLUME_ACTIVATION_TOOLS"></span>Volume Activation Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_Server_Backup"></span><span id="windows_server_backup"></span><span id="WINDOWS_SERVER_BACKUP"></span>Windows Server Backup
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Command_Line_Tools"></span><span id="command_line_tools"></span><span id="COMMAND_LINE_TOOLS"></span>Command Line Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Ink_Support"></span><span id="ink_support"></span><span id="INK_SUPPORT"></span>Ink Support
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Handwriting_Recognition"></span><span id="handwriting_recognition"></span><span id="HANDWRITING_RECOGNITION"></span>Handwriting Recognition
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Compact_Server"></span><span id="compact_server"></span><span id="COMPACT_SERVER"></span>Compact Server
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64"></span><span id="wow64"></span><span id="WOW64"></span>WoW64
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_.NET_Framework_2.0_and___________"></span><span id="wow64_for_.net_framework_2.0_and___________"></span><span id="WOW64_FOR_.NET_FRAMEWORK_2.0_AND___________"></span>WoW64 for .NET Framework 2.0 and PowerShell
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_.NET_Framework_2.0"></span><span id="wow64_for_.net_framework_2.0"></span><span id="WOW64_FOR_.NET_FRAMEWORK_2.0"></span>WoW64 for .NET Framework 2.0
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for___________"></span><span id="wow64_for___________"></span><span id="WOW64_FOR___________"></span>WoW64 for PowerShell
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_.NET_Framework_3.0_and_3.5"></span><span id="wow64_for_.net_framework_3.0_and_3.5"></span><span id="WOW64_FOR_.NET_FRAMEWORK_3.0_AND_3.5"></span>WoW64 for .NET Framework 3.0 and 3.5
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_Print_Services"></span><span id="wow64_for_print_services"></span><span id="WOW64_FOR_PRINT_SERVICES"></span>WoW64 for Print Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_Failover_Clustering"></span><span id="wow64_for_failover_clustering"></span><span id="WOW64_FOR_FAILOVER_CLUSTERING"></span>WoW64 for Failover Clustering
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_Input_Method_Editor"></span><span id="wow64_for_input_method_editor"></span><span id="WOW64_FOR_INPUT_METHOD_EDITOR"></span>WoW64 for Input Method Editor
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WoW64_for_Subsystem_for_UNIX-based_Applications"></span><span id="wow64_for_subsystem_for_unix-based_applications"></span><span id="WOW64_FOR_SUBSYSTEM_FOR_UNIX-BASED_APPLICATIONS"></span>WoW64 for Subsystem for UNIX-based Applications
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Desktop_Experience"></span><span id="desktop_experience"></span><span id="DESKTOP_EXPERIENCE"></span>Desktop Experience
</dt> <dd>

Added

</dd> <dt>

<span id="Server_Graphical_Shell"></span><span id="server_graphical_shell"></span><span id="SERVER_GRAPHICAL_SHELL"></span>Server Graphical Shell
</dt> <dd>

Added

</dd> <dt>

<span id="API_and_PowerShell_cmdlets"></span><span id="api_and_powershell_cmdlets"></span><span id="API_AND_POWERSHELL_CMDLETS"></span>API and PowerShell cmdlets
</dt> <dd>

Added

</dd> <dt>

<span id="SQL_Server_Connectivity"></span><span id="sql_server_connectivity"></span><span id="SQL_SERVER_CONNECTIVITY"></span>SQL Server Connectivity
</dt> <dd>

Added

</dd> <dt>

<span id="WSUS_Services"></span><span id="wsus_services"></span><span id="WSUS_SERVICES"></span>WSUS Services
</dt> <dd>

Added

</dd> <dt>

<span id="User_Interface_Management_Console"></span><span id="user_interface_management_console"></span><span id="USER_INTERFACE_MANAGEMENT_CONSOLE"></span>User Interface Management Console
</dt> <dd>

Added

</dd> <dt>

<span id="WID_Connectivity"></span><span id="wid_connectivity"></span><span id="WID_CONNECTIVITY"></span>WID Connectivity
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_PowerShell_2.0_Engine"></span><span id="windows_powershell_2.0_engine"></span><span id="WINDOWS_POWERSHELL_2.0_ENGINE"></span>Windows PowerShell 2.0 Engine
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_PowerShell_3.0"></span><span id="windows_powershell_3.0"></span><span id="WINDOWS_POWERSHELL_3.0"></span>Windows PowerShell 3.0
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_PowerShell_Web_Access"></span><span id="windows_powershell_web_access"></span><span id="WINDOWS_POWERSHELL_WEB_ACCESS"></span>Windows PowerShell Web Access
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_PowerShell_Desired_State_Configuration_Service"></span><span id="windows_powershell_desired_state_configuration_service"></span><span id="WINDOWS_POWERSHELL_DESIRED_STATE_CONFIGURATION_SERVICE"></span>Windows PowerShell Desired State Configuration Service
</dt> <dd>

Added

</dd> <dt>

<span id=".NET_Framework_4.5_Extended"></span><span id=".net_framework_4.5_extended"></span><span id=".NET_FRAMEWORK_4.5_EXTENDED"></span>.NET Framework 4.5 Extended
</dt> <dd>

Added

</dd> <dt>

<span id="WCF_Services"></span><span id="wcf_services"></span><span id="WCF_SERVICES"></span>WCF Services
</dt> <dd>

Added

</dd> <dt>

<span id="HTTP_Activation"></span><span id="http_activation"></span><span id="HTTP_ACTIVATION"></span>HTTP Activation
</dt> <dd>

Added

</dd> <dt>

<span id="Message_Queuing__MSMQ__Activation"></span><span id="message_queuing__msmq__activation"></span><span id="MESSAGE_QUEUING__MSMQ__ACTIVATION"></span>Message Queuing (MSMQ) Activation
</dt> <dd></dd> <dt>

<span id="Named_Pipe_Activation"></span><span id="named_pipe_activation"></span><span id="NAMED_PIPE_ACTIVATION"></span>Named Pipe Activation
</dt> <dd>

Added

</dd> <dt>

<span id="TCP_Activation"></span><span id="tcp_activation"></span><span id="TCP_ACTIVATION"></span>TCP Activation
</dt> <dd>

Added

</dd> <dt>

<span id="TCP_Port_Sharing"></span><span id="tcp_port_sharing"></span><span id="TCP_PORT_SHARING"></span>TCP Port Sharing
</dt> <dd>

Added

</dd> <dt>

<span id="ASP.NET_4.5"></span><span id="asp.net_4.5"></span>ASP.NET 4.5
</dt> <dd>

Added

</dd> <dt>

<span id=".NET_Extensibility_4.5"></span><span id=".net_extensibility_4.5"></span><span id=".NET_EXTENSIBILITY_4.5"></span>.NET Extensibility 4.5
</dt> <dd>

Added

</dd> <dt>

<span id="DirectAccess_and_VPN__RAS_"></span><span id="directaccess_and_vpn__ras_"></span><span id="DIRECTACCESS_AND_VPN__RAS_"></span>DirectAccess and VPN (RAS)
</dt> <dd>

Added

</dd> <dt>

<span id="Routing"></span><span id="routing"></span><span id="ROUTING"></span>Routing
</dt> <dd>

Added

</dd> <dt>

<span id="Storage_Services"></span><span id="storage_services"></span><span id="STORAGE_SERVICES"></span>Storage Services
</dt> <dd>

Added

</dd> <dt>

<span id="Failover_Cluster_Management_Tools"></span><span id="failover_cluster_management_tools"></span><span id="FAILOVER_CLUSTER_MANAGEMENT_TOOLS"></span>Failover Cluster Management Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Active_Directory_Rights_Management_Services_Tools"></span><span id="active_directory_rights_management_services_tools"></span><span id="ACTIVE_DIRECTORY_RIGHTS_MANAGEMENT_SERVICES_TOOLS"></span>Active Directory Rights Management Services Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Application_Initialization"></span><span id="application_initialization"></span><span id="APPLICATION_INITIALIZATION"></span>Application Initialization
</dt> <dd>

Added

</dd> <dt>

<span id="Centralized_SSL_Certificate_Support"></span><span id="centralized_ssl_certificate_support"></span><span id="CENTRALIZED_SSL_CERTIFICATE_SUPPORT"></span>Centralized SSL Certificate Support
</dt> <dd>

Added

</dd> <dt>

<span id="Claims-aware_Agent"></span><span id="claims-aware_agent"></span><span id="CLAIMS-AWARE_AGENT"></span>Claims-aware Agent
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Remote_Desktop_Session_Host_Tools"></span><span id="remote_desktop_session_host_tools"></span><span id="REMOTE_DESKTOP_SESSION_HOST_TOOLS"></span>Remote Desktop Session Host Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="WebSocket_Protocol"></span><span id="websocket_protocol"></span><span id="WEBSOCKET_PROTOCOL"></span>WebSocket Protocol
</dt> <dd>

no longer supported

</dd> <dt>

<span id="COM__Network_Access"></span><span id="com__network_access"></span><span id="COM__NETWORK_ACCESS"></span>COM+ Network Access
</dt> <dd>

No longer supported

</dd> <dt>

<span id="File_and_iSCSI_Services_name_change"></span><span id="file_and_iscsi_services_name_change"></span><span id="FILE_AND_ISCSI_SERVICES_NAME_CHANGE"></span>File and iSCSI Services name change
</dt> <dd>

Changed to File Services

</dd> </dl>

### Windows Server 2012

<dl> <dt>

<span id="User_Interfaces_and_Infrastructure"></span><span id="user_interfaces_and_infrastructure"></span><span id="USER_INTERFACES_AND_INFRASTRUCTURE"></span>User Interfaces and Infrastructure
</dt> <dd>

Added

</dd> <dt>

<span id="Server_for_NFS"></span><span id="server_for_nfs"></span><span id="SERVER_FOR_NFS"></span>Server for NFS
</dt> <dd>

Added

</dd> <dt>

<span id="File_Server_VSS_Agent_Service"></span><span id="file_server_vss_agent_service"></span><span id="FILE_SERVER_VSS_AGENT_SERVICE"></span>File Server VSS Agent Service
</dt> <dd>

Added

</dd> <dt>

<span id="iSCSI_Target_Server"></span><span id="iscsi_target_server"></span><span id="ISCSI_TARGET_SERVER"></span>iSCSI Target Server
</dt> <dd>

Added

</dd> <dt>

<span id="Data_Deduplication"></span><span id="data_deduplication"></span><span id="DATA_DEDUPLICATION"></span>Data Deduplication
</dt> <dd>

Added

</dd> <dt>

<span id="Work_Folders"></span><span id="work_folders"></span><span id="WORK_FOLDERS"></span>Work Folders
</dt> <dd>

Removed

</dd> <dt>

<span id="Core_Services"></span><span id="core_services"></span><span id="CORE_SERVICES"></span>Core Services
</dt> <dd>

Added for this version only.

</dd> <dt>

<span id="Remote_Desktop_Virtual_Graphics"></span><span id="remote_desktop_virtual_graphics"></span><span id="REMOTE_DESKTOP_VIRTUAL_GRAPHICS"></span>Remote Desktop Virtual Graphics
</dt> <dd>

Added for this version only

</dd> <dt>

<span id="Remote_Access"></span><span id="remote_access"></span><span id="REMOTE_ACCESS"></span>Remote Access
</dt> <dd>

Added

</dd> </dl>

### Windows Server 2008 R2

<dl> <dt>

<span id="UDDI_Services"></span><span id="uddi_services"></span><span id="UDDI_SERVICES"></span>UDDI Services
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_System_Resource_Manager"></span><span id="windows_system_resource_manager"></span><span id="WINDOWS_SYSTEM_RESOURCE_MANAGER"></span>Windows System Resource Manager
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Removable_Storage_Manager"></span><span id="removable_storage_manager"></span><span id="REMOVABLE_STORAGE_MANAGER"></span>Removable Storage Manager
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Windows_PowerShell"></span><span id="windows_powershell"></span><span id="WINDOWS_POWERSHELL"></span>Windows PowerShell
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Ink_and_Handwriting_Services"></span><span id="ink_and_handwriting_services"></span><span id="INK_AND_HANDWRITING_SERVICES"></span>Ink and Handwriting Services
</dt> <dd>

Added

</dd> <dt>

<span id="WinRM_IIS_Extension"></span><span id="winrm_iis_extension"></span><span id="WINRM_IIS_EXTENSION"></span>WinRM IIS Extension
</dt> <dd>

Added

</dd> <dt>

<span id="DirectAccess_Management_Console"></span><span id="directaccess_management_console"></span><span id="DIRECTACCESS_MANAGEMENT_CONSOLE"></span>DirectAccess Management Console
</dt> <dd>

Added

</dd> <dt>

<span id="Background_Intelligent_Transfer_Service__BITS_"></span><span id="background_intelligent_transfer_service__bits_"></span><span id="BACKGROUND_INTELLIGENT_TRANSFER_SERVICE__BITS_"></span>Background Intelligent Transfer Service (BITS)
</dt> <dd>

Added

</dd> <dt>

<span id="XPS_Viewer"></span><span id="xps_viewer"></span><span id="XPS_VIEWER"></span>XPS Viewer
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_Biometric_Framework"></span><span id="windows_biometric_framework"></span><span id="WINDOWS_BIOMETRIC_FRAMEWORK"></span>Windows Biometric Framework
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_Support"></span><span id="wow64_support"></span><span id="WOW64_SUPPORT"></span>WoW64 Support
</dt> <dd>

Added

</dd> <dt>

<span id="Windows_PowerShell_Integrated_Scripting_Environment__ISE_"></span><span id="windows_powershell_integrated_scripting_environment__ise_"></span><span id="WINDOWS_POWERSHELL_INTEGRATED_SCRIPTING_ENVIRONMENT__ISE_"></span>Windows PowerShell Integrated Scripting Environment (ISE)
</dt> <dd>

Added

</dd> <dt>

<span id="File_Replication_Service"></span><span id="file_replication_service"></span><span id="FILE_REPLICATION_SERVICE"></span>File Replication Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="BranchCache_for_Network_Files"></span><span id="branchcache_for_network_files"></span><span id="BRANCHCACHE_FOR_NETWORK_FILES"></span>BranchCache for Network Files
</dt> <dd>

Added

</dd> <dt>

<span id="Work_Folders"></span><span id="work_folders"></span><span id="WORK_FOLDERS"></span>Work Folders
</dt> <dd>

Added

</dd> <dt>

<span id="Distributed_Scan_Server"></span><span id="distributed_scan_server"></span><span id="DISTRIBUTED_SCAN_SERVER"></span>Distributed Scan Server
</dt> <dd>

Added

</dd> <dt>

<span id="FTP_Publishing_Service"></span><span id="ftp_publishing_service"></span><span id="FTP_PUBLISHING_SERVICE"></span>FTP Publishing Service
</dt> <dd>

No longer supported

</dd> <dt>

<span id="FTP_Management_Console"></span><span id="ftp_management_console"></span><span id="FTP_MANAGEMENT_CONSOLE"></span>FTP Management Console
</dt> <dd>

No longer supported

</dd> <dt>

<span id="FTP_Service"></span><span id="ftp_service"></span><span id="FTP_SERVICE"></span>FTP Service
</dt> <dd>

Added

</dd> <dt>

<span id="FTP_Extensibility"></span><span id="ftp_extensibility"></span><span id="FTP_EXTENSIBILITY"></span>FTP Extensibility
</dt> <dd>

Added

</dd> <dt>

<span id="IIS_Hostable_Web_Core"></span><span id="iis_hostable_web_core"></span><span id="IIS_HOSTABLE_WEB_CORE"></span>IIS Hostable Web Core
</dt> <dd></dd> <dt>

<span id="Windows_2000_Client_Support"></span><span id="windows_2000_client_support"></span><span id="WINDOWS_2000_CLIENT_SUPPORT"></span>Windows 2000 Client Support
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Certificate_Enrollment_Web_Service"></span><span id="certificate_enrollment_web_service"></span><span id="CERTIFICATE_ENROLLMENT_WEB_SERVICE"></span>Certificate Enrollment Web Service
</dt> <dd>

Added

</dd> <dt>

<span id="Certificate_Enrollment_Policy_Web_Service"></span><span id="certificate_enrollment_policy_web_service"></span><span id="CERTIFICATE_ENROLLMENT_POLICY_WEB_SERVICE"></span>Certificate Enrollment Policy Web Service
</dt> <dd>

Added

</dd> <dt>

<span id="UDDI_Services_Web_Application"></span><span id="uddi_services_web_application"></span><span id="UDDI_SERVICES_WEB_APPLICATION"></span>UDDI Services Web Application
</dt> <dd>

No longer supported

</dd> <dt>

<span id="UDDI_Services_Database"></span><span id="uddi_services_database"></span><span id="UDDI_SERVICES_DATABASE"></span>UDDI Services Database
</dt> <dd>

No longer supported

</dd> <dt>

<span id="Application_Server_Extensions_for_.NET_4.0"></span><span id="application_server_extensions_for_.net_4.0"></span><span id="APPLICATION_SERVER_EXTENSIONS_FOR_.NET_4.0"></span>Application Server Extensions for .NET 4.0
</dt> <dd>

Added

</dd> <dt>

<span id="UDDI_Services_Tools"></span><span id="uddi_services_tools"></span><span id="UDDI_SERVICES_TOOLS"></span>UDDI Services Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="BitLocker_Drive_Encryption_Administration_Utilities"></span><span id="bitlocker_drive_encryption_administration_utilities"></span><span id="BITLOCKER_DRIVE_ENCRYPTION_ADMINISTRATION_UTILITIES"></span>BitLocker Drive Encryption Administration Utilities
</dt> <dd>

Added

</dd> <dt>

<span id="AD_DS_and_AD_LDS_Tools"></span><span id="ad_ds_and_ad_lds_tools"></span><span id="AD_DS_AND_AD_LDS_TOOLS"></span>AD DS and AD LDS Tools
</dt> <dd>

No longer supported

</dd> <dt>

<span id="AD_DS_and_AD_LDS_Tools"></span><span id="ad_ds_and_ad_lds_tools"></span><span id="AD_DS_AND_AD_LDS_TOOLS"></span>AD DS and AD LDS Tools
</dt> <dd>

Added

</dd> <dt>

<span id="Active_Directory_Administrative_Center"></span><span id="active_directory_administrative_center"></span><span id="ACTIVE_DIRECTORY_ADMINISTRATIVE_CENTER"></span>Active Directory Administrative Center
</dt> <dd>

Added

</dd> <dt>

<span id="Active_Directory_module_for___________Windows_PowerShell"></span><span id="active_directory_module_for___________windows_powershell"></span><span id="ACTIVE_DIRECTORY_MODULE_FOR___________WINDOWS_POWERSHELL"></span>Active Directory module for Windows PowerShell
</dt> <dd>

Added

</dd> <dt>

<span id="Remote_Desktop_Connection_Broker_Tools"></span><span id="remote_desktop_connection_broker_tools"></span><span id="REMOTE_DESKTOP_CONNECTION_BROKER_TOOLS"></span>Remote Desktop Connection Broker Tools
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64"></span><span id="wow64"></span><span id="WOW64"></span>WoW64
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_.NET_Framework_2.0_and_Windows_PowerShell"></span><span id="wow64_for_.net_framework_2.0_and_windows_powershell"></span><span id="WOW64_FOR_.NET_FRAMEWORK_2.0_AND_WINDOWS_POWERSHELL"></span>WoW64 for .NET Framework 2.0 and Windows PowerShell
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_.NET_Framework_2.0"></span><span id="wow64_for_.net_framework_2.0"></span><span id="WOW64_FOR_.NET_FRAMEWORK_2.0"></span>WoW64 for .NET Framework 2.0
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for___________"></span><span id="wow64_for___________"></span><span id="WOW64_FOR___________"></span>WoW64 for PowerShell
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_.NET_Framework_3.0_and_3.5"></span><span id="wow64_for_.net_framework_3.0_and_3.5"></span><span id="WOW64_FOR_.NET_FRAMEWORK_3.0_AND_3.5"></span>WoW64 for .NET Framework 3.0 and 3.5
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_Print_Services"></span><span id="wow64_for_print_services"></span><span id="WOW64_FOR_PRINT_SERVICES"></span>WoW64 for Print Services
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_Failover_Clustering"></span><span id="wow64_for_failover_clustering"></span><span id="WOW64_FOR_FAILOVER_CLUSTERING"></span>WoW64 for Failover Clustering
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_Input_Method_Editor"></span><span id="wow64_for_input_method_editor"></span><span id="WOW64_FOR_INPUT_METHOD_EDITOR"></span>WoW64 for Input Method Editor
</dt> <dd>

Added

</dd> <dt>

<span id="WoW64_for_Subsystem_for_UNIX-based_Applications"></span><span id="wow64_for_subsystem_for_unix-based_applications"></span><span id="WOW64_FOR_SUBSYSTEM_FOR_UNIX-BASED_APPLICATIONS"></span>WoW64 for Subsystem for UNIX-based Applications
</dt> <dd>

Added

</dd> <dt>

<span id="BitLocker_Recovery_Password_Viewer"></span><span id="bitlocker_recovery_password_viewer"></span><span id="BITLOCKER_RECOVERY_PASSWORD_VIEWER"></span>BitLocker Recovery Password Viewer
</dt> <dd>

Added

</dd> <dt>

<span id="Print_and_Document_Services_name_change"></span><span id="print_and_document_services_name_change"></span><span id="PRINT_AND_DOCUMENT_SERVICES_NAME_CHANGE"></span>Print and Document Services name change
</dt> <dd>

named Print Services for this release

</dd> <dt>

<span id="Remote_Desktop_Services_name_change"></span><span id="remote_desktop_services_name_change"></span><span id="REMOTE_DESKTOP_SERVICES_NAME_CHANGE"></span>Remote Desktop Services name change
</dt> <dd>

named Terminal Services in this release

</dd> <dt>

<span id=".NET_Framework_3.5.1_Features_name_change"></span><span id=".net_framework_3.5.1_features_name_change"></span><span id=".NET_FRAMEWORK_3.5.1_FEATURES_NAME_CHANGE"></span>.NET Framework 3.5.1 Features name change
</dt> <dd>

Named .NET Framework 3.0 Features in this release

</dd> <dt>

<span id="Remote_Desktop_Session_Host_name_change"></span><span id="remote_desktop_session_host_name_change"></span><span id="REMOTE_DESKTOP_SESSION_HOST_NAME_CHANGE"></span>Remote Desktop Session Host name change
</dt> <dd>

Named Terminal Server in this release

</dd> <dt>

<span id="Remote_Desktop_Licensing_name_change"></span><span id="remote_desktop_licensing_name_change"></span><span id="REMOTE_DESKTOP_LICENSING_NAME_CHANGE"></span>Remote Desktop Licensing name change
</dt> <dd>

Named TS Licensing in this release

</dd> <dt>

<span id="Remote_Desktop_Gateway_name_change"></span><span id="remote_desktop_gateway_name_change"></span><span id="REMOTE_DESKTOP_GATEWAY_NAME_CHANGE"></span>Remote Desktop Gateway name change
</dt> <dd>

Named TS Gateway in this release

</dd> <dt>

<span id="Remote_Desktop_Connection_Broker_name_change"></span><span id="remote_desktop_connection_broker_name_change"></span><span id="REMOTE_DESKTOP_CONNECTION_BROKER_NAME_CHANGE"></span>Remote Desktop Connection Broker name change
</dt> <dd>

Named TS Session Broker in this release

</dd> <dt>

<span id="Remote_Desktop_Web_Access_name_change"></span><span id="remote_desktop_web_access_name_change"></span><span id="REMOTE_DESKTOP_WEB_ACCESS_NAME_CHANGE"></span>Remote Desktop Web Access name change
</dt> <dd>

Named TS Web Access in this release

</dd> <dt>

<span id=".NET_Framework_3.5.1_name_change"></span><span id=".net_framework_3.5.1_name_change"></span><span id=".NET_FRAMEWORK_3.5.1_NAME_CHANGE"></span>.NET Framework 3.5.1 name change
</dt> <dd>

(220) Named Net FX 3.0 Features in this release

(230) Named Application Server Core in this release

</dd> <dt>

<span id="AD_DS_Tools_name_change"></span><span id="ad_ds_tools_name_change"></span><span id="AD_DS_TOOLS_NAME_CHANGE"></span>AD DS Tools name change
</dt> <dd>

Named Active Directory Domain Services Tools in this release

</dd> <dt>

<span id="AD_LDS_Snap-Ins_and_Command-Line_Tools_name_change"></span><span id="ad_lds_snap-ins_and_command-line_tools_name_change"></span><span id="AD_LDS_SNAP-INS_AND_COMMAND-LINE_TOOLS_NAME_CHANGE"></span>AD LDS Snap-Ins and Command-Line Tools name change
</dt> <dd>

Named Active Directory Lightweight Directory Services Tools in this release

</dd> <dt>

<span id="Print_and_Document_Services_Tools_name_change"></span><span id="print_and_document_services_tools_name_change"></span><span id="PRINT_AND_DOCUMENT_SERVICES_TOOLS_NAME_CHANGE"></span>Print and Document Services Tools name change
</dt> <dd>

Named Print Services Tools in this release

</dd> <dt>

<span id="Remote_Desktop_Services_Tools_name_change"></span><span id="remote_desktop_services_tools_name_change"></span><span id="REMOTE_DESKTOP_SERVICES_TOOLS_NAME_CHANGE"></span>Remote Desktop Services Tools name change
</dt> <dd>

Named Terminal Services Tools in this release

</dd> <dt>

<span id="Remote_Desktop_Session_Host_Tools_name_change"></span><span id="remote_desktop_session_host_tools_name_change"></span><span id="REMOTE_DESKTOP_SESSION_HOST_TOOLS_NAME_CHANGE"></span>Remote Desktop Session Host Tools name change
</dt> <dd>

Named Terminal Server Tools in this release

</dd> <dt>

<span id="Remote_Desktop_Gateway_Tools_name_change"></span><span id="remote_desktop_gateway_tools_name_change"></span><span id="REMOTE_DESKTOP_GATEWAY_TOOLS_NAME_CHANGE"></span>Remote Desktop Gateway Tools name change
</dt> <dd>

Named TS Gateway Tools in this release

</dd> <dt>

<span id="Remote_Desktop_Licensing_Tools_name_change"></span><span id="remote_desktop_licensing_tools_name_change"></span><span id="REMOTE_DESKTOP_LICENSING_TOOLS_NAME_CHANGE"></span>Remote Desktop Licensing Tools name change
</dt> <dd>

Named TS Licensing Tools in this release

</dd> <dt>

<span id="AD_DS_Snap-Ins_and_Command-Line_Tools_name_change"></span><span id="ad_ds_snap-ins_and_command-line_tools_name_change"></span><span id="AD_DS_SNAP-INS_AND_COMMAND-LINE_TOOLS_NAME_CHANGE"></span>AD DS Snap-Ins and Command-Line Tools name change
</dt> <dd>

Active Directory Domain Controller Tools

</dd> </dl>

## Examples

The following script displays the names of all the server features on the computer named "FABRIKAM". Note that the target computer must be running Windows Server 2008 or a later server operating system.


```VB
strComputer = "FABRIKAM"

Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")

Set colFeatureList = objWMIService.ExecQuery("SELECT Name FROM Win32_ServerFeature")

For Each objFeature In colFeatureList
   WScript.Echo objFeature.Name

Next
```



## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>ServerCompProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerCompProv.dll</dt> </dl> |



 

 




