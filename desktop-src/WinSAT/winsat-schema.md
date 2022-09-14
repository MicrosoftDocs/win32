---
title: WinSAT Schema
description: You can use the Windows System Assessment Tool (WinSAT) schema to determine valid XPath queries to run.
ms.assetid: da497f3b-f5a2-401e-8230-937362ecf4f2
ms.topic: article
ms.date: 05/31/2018
---

# WinSAT Schema

\[WinSAT enumerations may be altered or unavailable for releases after Windows 8.1.\]

You can use the Windows System Assessment Tool (WinSAT) schema to determine valid XPath queries to run. To run an XPath query, see one of the following methods:

-   [**IQueryAllWinSATAssessments::get\_AllXML**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryallwinsatassessments-get_allxml)
-   [**IQueryRecentWinSATAssessment::get\_XML**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryrecentwinsatassessment-get_xml)

The **WinSAT** element can have a **WinsatAssessments** element as a parent element when you call the [**get\_AllXML**](/windows/desktop/api/Winsatcominterfacei/nf-winsatcominterfacei-iqueryallwinsatassessments-get_allxml) method.

The following is the WinSAT schema that you can use to determine the XPath.


```xsd
<?xml version="1.0" encoding="utf-16" ?>                                
<xsd:schema elementFormDefault="qualified"            
            xmlns:xsd="https://www.w3.org/2001/XMLSchema"> 

  <!-- Defines an assessment. -->   
  <xsd:element name="WinSAT">
    <xsd:complexType>      
      <xsd:sequence>

         <!-- Indicates if the command line contained the -v flag. -->
         <xsd:element name="Verbose" type="xsd:boolean"/>

         <!-- Defines information about the WinSAT program that generated -->
         <!-- the assessment. -->
         <xsd:element name="ProgramInfo" >
           <xsd:complexType>
             <xsd:sequence>
               <xsd:element name="Name" type="xsd:string"/>                             
               <xsd:element name="Version" type="xsd:string"/>               
               <xsd:element name="Title" type="xsd:string"/>               
               <xsd:element name="ModulePath" type="xsd:string"/>              
               <xsd:element name="CmdLine" type="xsd:string"/> 

               <!-- The string that was passed using the -note flag in -->
               <!-- the command line. -->
               <xsd:element name="Note" type="xsd:string" />
             </xsd:sequence>
           </xsd:complexType>
         </xsd:element>

         <!-- Contains child elements that define the base score -->
         <!-- and scores for the subcomponents of the assessment. -->
         <!-- If the assessment is a formal assessment (the XML document -->
         <!-- contains an <IsFormal> element), each child element will contain -->
         <!-- a nonzero text value that represents the score. If the -->
         <!-- assessment is an ad hoc assessment for a subcomponent of the -->
         <!-- assessment, such as memory, then only the child element for -->
         <! --the subcomponent being assessed will contain a nonzero value. -->
         <!-- The child elements of interest are: -->
         <!--    SystemScore   - Base score for the computer -->
         <!--    MemoryScore   - Memory score -->
         <!--    CpuScore      - Processor score -->
         <!--    GraphicsScore - Video card score -->
         <!--    GamingScore   - D3D graphics score -->
         <!--    DiskScore     - Primary disk score -->

         <xsd:element ref="WinSPR" minOccurs="0" maxOccurs="1" />

         <!-- Contains child elements that group the engineering units (metrics) -->
         <!-- for each subcomponent; the scores are a function of the metrics. -->
         <!-- If the assessment is a formal assessment (the XML document -->
         <!-- contains an <IsFormal> element), each metrics group will contain -->
         <!-- metric data. If the assessment is an ad hoc assessment for a -->
         <!-- subcomponent of the assessment, such as memory, then only that -->
         <!-- metrics group will contain metric data. -->
         <!-- The child elements (metrics groups) are: -->
         <!--    CPUMetrics -->
         <!--    MemoryMetrics -->
         <!--    GamingMetrics -->
         <!--    GraphicMetrics -->
         <!--    DiskMetrics -->

         <!-- The CPUMetrics group contains the following child elements, -->
         <!-- which contain the metrics data. The metrics data for each -->
         <!-- child element corresponds to a command-line argument. -->
         <!-- The arguments shown are those used by the formal assessment. -->
         <!-- Each child element contains a "units" attribute whose value -->
         <!-- is the unit of measurement for the metric, for example, MB/s. -->
         <!--    CompressionMetric -->
         <!--       argument: cpu -compression -->
         <!--    EncryptionMetric -->
         <!--       argument: cpu -encryption -->
         <!--    Compression2Metric -->
         <!--       argument: cpu -compression2 -->
         <!--    Encryption2Metric -->
         <!--       argument: cpu -encryption2 -->
         <!--    DshowEncodeTime -->
         <!--       argument: media -input {winsatencode.wmv} -encode {winsat.prx} -->
 
         <!-- The MemoryMetrics group contains the following child elements, -->
         <!-- which contain the metrics data. The metrics data for each -->
         <!-- child element corresponds to a command-line argument. -->
         <!-- The arguments shown are those used by the formal assessment. -->
         <!-- Each child element contains a "units" attribute whose value -->
         <!-- is the unit of measurement for the metric, for example, MB/s. -->
         <!--    Bandwidth -->
         <!--       argument: mem -->

         <!-- The GamingMetrics group contains the following child elements, -->
         <!-- which contain the metrics data. The metrics data for each -->
         <!-- child element corresponds to a command-line argument. -->
         <!-- The arguments shown are those used by the formal assessment. -->
         <!-- Each child element contains a "units" attribute whose value -->
         <!-- is the unit of measurement for the metric, for example, F/s. -->
         <!--    AlphaFps -->
         <!--       argument: -aname Alpha -time  5 -fbc 10 -nodisp -animate 10 -->
         <!--                 -width 1280 -height 1024 -totalobj 2000 -batchcnt C(500) -->
         <!--                 -rendertotex 6 -rtdelta 3 -texpobj C(1) -->
         <!--    ALUFps -->
         <!--       argument: -aname ALU -time  5 -fbc 10 -nodisp -animate 10 -->
         <!--                 -width 1280 -height 1024 -totalobj 2000 -batchcnt C(500) -->
         <!--                 -noalpha -alushader -totaltex 10  -texpobj C(1) -->
         <!--                 -rendertotex 6 -rtdelta 3 -->
         <!--    TexFps -->
         <!--       argument: -aname Tex -time  5 -fbc 10 -nodisp -animate 10 -->
         <!--                 -width 1280 -height 1024 -totalobj 2000 -batchcnt C(500) -->
         <!--                 -noalpha -texshader -totaltex 10 -texpobj C(4) -->
         <!--                 -rendertotex 6 -rtdelta 3 -->

         <!-- The GraphicsMetrics group contains the following child elements, -->
         <!-- which contain the metrics data. The metrics data for each -->
         <!-- child element corresponds to a command-line argument. -->
         <!-- The arguments shown are those used by the formal assessment. -->
         <!-- Each child element contains a "units" attribute whose value -->
         <!-- is the unit of measurement for the metric, for example, F/s. -->
         <!--    DWMFps -->
         <!--       argument: dwm -fbc 10 -time 10 -nodisp -normalw 12 -width 1280 -->
         <!--                 -height 1024 -winwidth C(1144) -winheight C(915) -->
         <!--                 -rendertotex 6 -rtdelta 3 -nolock -->
         <!--    VideoMemBandwidth -->
         <!--       argument: dwm -fbc 10 -time 10 -nodisp -normalw 12 -width 1280 -->
         <!--                 -height 1024 -winwidth C(1144) -winheight C(915) -->
         <!--                 -rendertotex 6 -rtdelta 3 -nolock -->
         <!--    MFVideoDecodeDur -->
         <!--       argument: mfmedia -input {winsat.wmv} -nopmp -->

         <!-- The DiskMetrics group contains the following child elements, -->
         <!-- which contain the metrics data. The metrics data for each -->
         <!-- child element corresponds to a command-line argument. -->
         <!-- The arguments shown are those used by the formal assessment. -->
         <!-- Each child element contains a "units" attribute whose value -->
         <!-- is the unit of measurement for the metric, for example, MB/s. -->
         <!--    AvgThroughput -->
         <!--       argument: "disk -seq -read -n %u" where %u is the disk number -->
         <!--                 associated with the system drive. -->

         <xsd:element ref="Metrics" minOccurs="0" maxOccurs="1" />

         <!-- Date and time that the assessment ran -->
         <xsd:element name="ExecDateTOD" type="FullDateTime"/>

         <!-- The assessment was generated by a released version of WinSAT -->
         <!-- The text value is 1 if official; otherwise, 0. -->
         <xsd:element name="IsOfficial" type="xsd:string" />

         <!-- The element exists if the assessment is a formal assessment. -->
         <!-- The element does not exist if the assessment is an ad hoc assessment. -->
         <xsd:element name="IsFormal" type="xsd:string" minOccurs="0" maxOccurs="1"/>

         <!-- The element exists if the assessment is the initial assessment -->
         <!-- that ran during the out-of-box experience (when the user set up -->
         <!-- the computer for the first time). -->
         <xsd:element name="IsMoobe" type="xsd:string" minOccurs="0" maxOccurs="1"/>

         <!-- The text value is 1 if true; otherwise, 0. -->
         <xsd:element name="RanOverTs" type="xsd:string" />
         <xsd:element name="RanOnBatteries" type="xsd:string" />

         <xsd:element name ="Iteration" type="xsd:string" maxOccurs="1" minOccurs="0"/>
         <xsd:element name ="GUID" type="xsd:string" maxOccurs="1" minOccurs="0"/>

         <!-- Group that defines the computer's hardware configuration. The -->
         <!-- data in this group is not used in generating the metrics. -->
         <xsd:element name="SystemConfig" type="SystemConfigType"/>                

         <!-- Time it took to gather the computer's hardware configuration -->
         <!-- information. -->
         <xsd:element ref="AssessmentRunTime" />

         <!-- Subcomponent assessments groups that contain the data used -->
         <!-- to generate the metrics. -->
         <xsd:sequence minOccurs="0" maxOccurs="unbounded">
          <xsd:choice>
            <xsd:element name="SystemMemoryBandwidth" type="SystemMemoryBandwidthType" />
            <xsd:element name="DiskAssessment" type="DiskAssessmentType" />
            <xsd:element name="CPUEncryptionAssessment" type="CPUMPAssessmentType" />
            <xsd:element name="CPUEncryption2Assessment" type="CPUMPAssessmentType" />
            <xsd:element name="CPUCRC32Assessment" type="CPUMPAssessmentType" />
            <xsd:element name="CPUCompressionAssessment" type="CPUMPAssessmentType" />
            <xsd:element name="CPUCompression2Assessment" type="CPUMPAssessmentType" />
            <xsd:element name="GraphicsResultGroup" type="GraphicsResultGroupType" />
            <xsd:element name="DshowEncode" type="MediaEncodeType" />
            <xsd:element name="DshowDecode" type="MediaDecodeType" />
            <xsd:element name="MediaFoundationDecode" type="MediaDecodeType" />
          </xsd:choice>               

         <!-- Time it took to run the subcomponent's assessment. -->
          <xsd:element ref="AssessmentRunTime" />
           </xsd:sequence>      

         <!-- Completion status of the assessment. Each subcomponent also -->
         <!-- provides a completion status for the subcomponent. -->
         <xsd:element name="CompletionStatus" type="CompletionStatusType"/>

         <!-- Time it took to run the assessment. -->
         <xsd:element name="TotalRunTime" >
            <xsd:complexType>
              <xsd:sequence>
                <xsd:element name="Seconds" type="xsd:string" />
                <xsd:element name="Description" type="xsd:string" />
              </xsd:sequence>
            </xsd:complexType>
         </xsd:element>
      </xsd:sequence>
    </xsd:complexType>
  </xsd:element>  <!-- End of WinSAT element definition -->

  <xsd:element name="TestData" >
      <xsd:complexType>
          <xsd:sequence>
             <xsd:any maxOccurs="unbounded" processContents="skip"/>    
          </xsd:sequence>
      </xsd:complexType>
  </xsd:element>

  <xsd:element name="Metrics" >
      <xsd:complexType>
          <xsd:sequence>
             <xsd:any maxOccurs="unbounded" processContents="skip"/>    
          </xsd:sequence>
      </xsd:complexType>
  </xsd:element>

  <xsd:element name="WinSPR" >
      <xsd:complexType>
          <xsd:sequence>
             <xsd:any maxOccurs="unbounded" processContents="skip"/>    
          </xsd:sequence>
      </xsd:complexType>
  </xsd:element>

  <xsd:element name="AssessmentRunTime" >
      <xsd:complexType>
            <xsd:sequence>
              <xsd:element name="Seconds" type="xsd:string" />
              <xsd:element name="Description" type="xsd:string" />
            </xsd:sequence>
     </xsd:complexType>
 </xsd:element>

  <xsd:complexType name="SequenceWMIInstance">
    <xsd:sequence>
      <xsd:element name="Instance" minOccurs="0" maxOccurs="unbounded" type="WMIInstance"/>
    </xsd:sequence>    
  </xsd:complexType>
  
  <xsd:complexType name="WMIInstance">
    <xsd:sequence>
      <xsd:any maxOccurs="unbounded" processContents="skip"/>
    </xsd:sequence>
    <xsd:attribute name="id" type="xsd:string"/>
  </xsd:complexType>
  
  <xsd:complexType name="OperationVersionType">    
    <xsd:attribute name="Major" type="xsd:string"/>
    <xsd:attribute name="Minor" type="xsd:string"/>
    <xsd:attribute name="Build" type="xsd:string"/>
    <xsd:attribute name="Revision" type="xsd:string"/>
  </xsd:complexType>  
  
    <xsd:complexType name ="FullDateTime">
      <xsd:simpleContent>
        <xsd:extension base="xsd:string">
           <xsd:attribute name="Friendly" />               
        </xsd:extension>                
      </xsd:simpleContent>
    </xsd:complexType>

  <xsd:complexType name="UnitsType">
      <xsd:attribute name="name" type="xsd:string" />
      <xsd:attribute name="units" type="xsd:string" />
      <xsd:attribute name="descrip" type="xsd:string" />
  </xsd:complexType>

  <xsd:complexType name="CPUManufacturer">
          <xsd:simpleContent>
             <xsd:extension base="xsd:string">              
                 <xsd:attribute name="friendly" /> 
             </xsd:extension>                
          </xsd:simpleContent>
   </xsd:complexType>


  <xsd:complexType name="SystemConfigType">
    <xsd:sequence>

      <xsd:element name ="ComputerName" type="xsd:string" maxOccurs="1" minOccurs="0"/>

      <xsd:element name="OSVersion" minOccurs="1"  maxOccurs="1"> 
        <xsd:complexType>
            <xsd:sequence >
              <xsd:element name="Major" type="xsd:string"/>              
              <xsd:element name="Minor" type="xsd:string"/>
              <xsd:element name="Build" type="xsd:string"/>
              <xsd:element name="ProductType" type="xsd:string"/>
              <xsd:element name="ProductName" type="xsd:string"/>
              <xsd:element name="OSName" type="xsd:string"/>
              <xsd:element name="BuildLab" minOccurs="0" type="xsd:string"/>
              </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="Platform"> 
        <xsd:complexType>
            <xsd:sequence >
              <xsd:element name="IsMobile" type="xsd:string" minOccurs="0"  maxOccurs="1"/>              

              <xsd:element name="PlatformRole" minOccurs="0"  maxOccurs="1">
                <xsd:complexType>
                  <xsd:simpleContent>
                      <xsd:extension base="xsd:string">
                      <xsd:attribute name="desc" />               
                    </xsd:extension>                
                  </xsd:simpleContent>
                </xsd:complexType>
              </xsd:element>

              </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="Processor">
        <xsd:complexType>
          <xsd:sequence maxOccurs="unbounded">
            <xsd:element name="Instance" >        
              <xsd:complexType>
                <xsd:sequence>
                  <xsd:element name ="ProcessorName" type="xsd:string"/>
                  <xsd:element name ="TSCFrequency" type="xsd:string"/>
                  <xsd:element name ="NumProcs" type="xsd:string"/>
                  <xsd:element name ="NumCores" type="xsd:string"/>
                  <xsd:element name ="NumCPUs" type="xsd:string"/>
                  <xsd:element name ="NumCPUsPerCore" type="xsd:string"/>
                  <xsd:element name ="NumCoresPerProcessor" type="xsd:string"/>
                  <xsd:element name ="CoresAreThreaded" type="xsd:string"/>
                  <xsd:element name ="X64Capable" type="xsd:string"/>
                  <xsd:element name ="X64Running" type="xsd:string"/>
                  <xsd:element name ="Signature" >
                    <xsd:complexType>
                      <xsd:sequence>
                        <xsd:element name="Manufacturer" type="CPUManufacturer" />
                        <xsd:element name="Stepping" type="xsd:string" />
                        <xsd:element name="Model" type="xsd:string" />
                        <xsd:element name="Family" type="xsd:string" />
                        <xsd:element name="ExtendedModel" type="xsd:string" />
                        <xsd:element name="ExtendedFamily" type="xsd:string" />
                        <xsd:element name="CompactSignature" type="xsd:string"/>     
                      </xsd:sequence>
                    </xsd:complexType>
                  </xsd:element>
                  <xsd:element name ="L1Cache" >
                    <xsd:complexType>
                      <xsd:sequence>
                        <xsd:element name="Size" type="xsd:string" />
                        <xsd:element name="Ways" type="xsd:string" />
                        <xsd:element name="LineSize" type="xsd:string" />
                        <xsd:element name="SectorSize" type="xsd:string" />                  
                      </xsd:sequence>
                    </xsd:complexType>
                  </xsd:element>
                  <xsd:element name ="L2Cache" >
                    <xsd:complexType>
                      <xsd:sequence>
                        <xsd:element name="Size" type="xsd:string" />
                        <xsd:element name="Ways" type="xsd:string" />
                        <xsd:element name="LineSize" type="xsd:string" />
                        <xsd:element name="SectorSize" type="xsd:string" />                  
                      </xsd:sequence>
                    </xsd:complexType>
                  </xsd:element>
                  <xsd:element name="MMX" type="xsd:string"/>               
                  <xsd:element name="SSE" type="xsd:string"/>               
                  <xsd:element name="SSE2" type="xsd:string"/>               

                  <xsd:element name ="LogicalProcessorInfo" maxOccurs="unbounded" minOccurs="0">
                      <xsd:complexType>
                          <xsd:sequence>
                             <xsd:any maxOccurs="unbounded" processContents="skip"/>    
                          </xsd:sequence>
                      </xsd:complexType>
                  </xsd:element>

                </xsd:sequence> 
                <xsd:attribute name="id" type="xsd:string"/>                       
              </xsd:complexType>        
            </xsd:element>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>      

      <xsd:element name="Memory">
        <xsd:complexType>
            <xsd:sequence minOccurs="1" maxOccurs="1">

            <xsd:element name="TotalPhysical" minOccurs="1" maxOccurs="1">
              <xsd:complexType>
                  <xsd:sequence>
                     <xsd:element name="Size" type="xsd:string"/>               
                     <xsd:element name="Bytes" type="xsd:string"/>               
                  </xsd:sequence>
              </xsd:complexType>
            </xsd:element>

            <xsd:element name="AvailablePhysical" minOccurs="1" maxOccurs="1">
                <xsd:complexType>
                    <xsd:sequence>
                       <xsd:element name="Size" type="xsd:string"/>               
                       <xsd:element name="Bytes" type="xsd:string"/>               
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>

            <xsd:element name="Modules" type="SequenceWMIInstance" minOccurs="0"/>

            </xsd:sequence>
        </xsd:complexType>
      </xsd:element>      

<xsd:element name="Monitors">
        <xsd:complexType>

            <xsd:sequence>
                <xsd:element name="Count" type="xsd:string"/>              
                <xsd:element name="TotalMonitorPixels" type="xsd:string"/>              
                <xsd:element name="Monitor" minOccurs="1" maxOccurs="unbounded">
                  <xsd:complexType>
                     <xsd:sequence >
                        <xsd:element name="DeviceName" type="xsd:string"/>              
                       <xsd:element name="Width" type="xsd:string"/>              
                      <xsd:element name="Height" type="xsd:string"/>
                      <xsd:element name="TotalMonitorPixels" type="xsd:string"/>
                   </xsd:sequence>

                  <xsd:attribute name="id" type="xsd:string" />
                  <xsd:attribute name="primary" type="xsd:string" />
                 </xsd:complexType>
                </xsd:element>      
            </xsd:sequence>
         </xsd:complexType>
       </xsd:element>

      <xsd:element name="Graphics">
        <xsd:complexType>
          <xsd:sequence minOccurs="0">
            <xsd:element name="AdapterDescription" type="xsd:string"/>
            <xsd:element name="AdapterManufacturer" type="xsd:string"/>
            <xsd:element name="DriverVersion">
              <xsd:complexType>
                <xsd:simpleContent>
                  <xsd:extension base="xsd:string">
                     <xsd:attribute name="Friendly" />               
                  </xsd:extension>                
                </xsd:simpleContent>
              </xsd:complexType>
            </xsd:element>
            <xsd:element name="DriverDate" type="FullDateTime"/>

            <xsd:element name="DedicatedVideoMemory" type="xsd:string"/>
            <xsd:element name="DedicatedSystemMemory" type="xsd:string"/>
            <xsd:element name="SharedSystemMemory" type="xsd:string"/>

            <xsd:element name="Suports32BitsPerPixel" type="xsd:string"/>
            <xsd:element name="D3D9OrBetter" type="xsd:string"/>
            <xsd:element name="VertexShaderProfile" type="xsd:string"/>
            <xsd:element name="PixelShaderProfile" type="xsd:string"/>
            <xsd:element name="PixelShader2OrBetter" type="xsd:string"/>
            <xsd:element name="PixelShader3OrBetter" type="xsd:string"/>
            <xsd:element name="LDDM" type="xsd:string"/>
            <xsd:element name="WHQL" type="xsd:string"/>
            <xsd:element name="PNPID" type="xsd:string"/>
            <xsd:element name="DWMRunningOnStart" type="xsd:string"/>
            <xsd:element name="DWMRunning" type="xsd:string"/>
          </xsd:sequence>            
        </xsd:complexType>
      </xsd:element>      
      <xsd:element name="Disk" type="SequenceWMIInstance" minOccurs="0"/>

      <xsd:element name="TPM" minOccurs="0"  maxOccurs="1">
        <xsd:complexType>
          <xsd:sequence >
            <xsd:element name="ManufacturerId" type="xsd:string"/>
            <xsd:element name="ManufacturerVersion" type="xsd:string"/>
            <xsd:element name="ManufacturerVersionInfo" type="xsd:string"/>
            <xsd:element name="PhysicalPresenceVersionInfo" type="xsd:string"/>
            <xsd:element name="SpecVersion" type="xsd:string"/>
            <xsd:element name="IsActivated" type="xsd:string"/>
            <xsd:element name="IsEnabled" type="xsd:string"/>
            <xsd:element name="IsEndorsementKeyPairPresent" type="xsd:string"/>
            <xsd:element name="IsOwned" type="xsd:string"/>
            <xsd:element name="IsOwnerClearDisabled" type="xsd:string"/>
            <xsd:element name="IsOwnershipAllowed" type="xsd:string"/>
            <xsd:element name="IsPhysicalClearDisabled" type="xsd:string"/>
            <xsd:element name="IsPhysicalPresenceHardwareEnabled" type="xsd:string"/>
            <xsd:element name="IsSrkAuthCompatible" type="xsd:string"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="DiscRecorder" minOccurs="0"  maxOccurs="1">
        <xsd:complexType>
          <xsd:sequence minOccurs="1" maxOccurs="unbounded">
            <xsd:element name="Instance">
              <xsd:complexType>
                <xsd:sequence >
                  <xsd:element name="DevicePath" type="xsd:string"/>
                  <xsd:element name="CanLoadMedia" type="xsd:string" minOccurs="0"/>
                  <xsd:element name="Vendor" type="xsd:string"/>
                  <xsd:element name="ProductId" type="xsd:string"/>
                  <xsd:element name="ProductRevision" type="xsd:string"/>
                  <xsd:element name="VolumePath" type="xsd:string"/>
                  <xsd:element name="SupportedProfiles" type="xsd:string"/>
                  <xsd:element name="CDWriteSpeeds" type="xsd:string"/>
                  <xsd:element name="DVDWriteSpeeds" type="xsd:string" minOccurs="0"/>
                </xsd:sequence>
                <xsd:attribute name="id" type="xsd:string" />
              </xsd:complexType>
            </xsd:element>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="Scanner" minOccurs="0"  maxOccurs="1">
        <xsd:complexType>
          <xsd:sequence minOccurs="1" maxOccurs="unbounded">
            <xsd:element name="Instance">
              <xsd:complexType>
                <xsd:sequence >
                  <xsd:element name="Vendor" type="xsd:string"/>
                  <xsd:element name="DeviceName" type="xsd:string"/>
                  <xsd:element name="Port" type="xsd:string"/>
                  <xsd:element name="DriverVersion" type="xsd:string"/>
                  <xsd:element name="ConnectionType" type="xsd:string"/>
                </xsd:sequence>
                <xsd:attribute name="id" type="xsd:string" />
              </xsd:complexType>
            </xsd:element>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="Modem" minOccurs="0"  maxOccurs="1">
        <xsd:complexType>
          <xsd:sequence minOccurs="1" maxOccurs="unbounded">
            <xsd:element name="Instance">
              <xsd:complexType>
                <xsd:sequence >
                  <xsd:element name="DevicePath" type="xsd:string"/>
                  <xsd:element name="FriendlyName" type="xsd:string"/>
                  <xsd:element name="Port" type="xsd:string"/>
                  <xsd:element name="MaxOutputBufferSize" type="xsd:string"/>
                  <xsd:element name="MaxInputBufferSize" type="xsd:string"/>
                  <xsd:element name="BaudRate" type="xsd:string"/>
                </xsd:sequence>
                <xsd:attribute name="id" type="xsd:string" />
              </xsd:complexType>
            </xsd:element>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="Digitizer" minOccurs="0"  maxOccurs="1" type="xsd:string"/>
    </xsd:sequence>    
  </xsd:complexType>
   
  <xsd:complexType name="SystemMemoryBandwidthType">  
    <xsd:sequence>
      <xsd:element name="TestName" type="xsd:string" />
      <xsd:element name="OperationVersion" type="OperationVersionType" />
      <xsd:sequence minOccurs="0" maxOccurs="1">
          <xsd:element name="Units" type="UnitsType" minOccurs="2" maxOccurs="2"/>     
          <xsd:element name="NumProcessors" type="xsd:string" />
          <xsd:element name="NumThreads" type="xsd:string" />     
          <xsd:element name="PageSize">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">
                  <xsd:attribute name="UnCachedMemSpace" />               
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="MemBlockSize">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">
                  <xsd:attribute name="UnCachedMemSpace" />               
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="MemDestOffset">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">              
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="TotalBytesPerSecond">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">              
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>     
          <xsd:element name="TotalBytesPerSecondMean">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">              
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>     
          <xsd:element ref="TestData" minOccurs="0" maxOccurs="1" />
          <xsd:element name="PerCPUData">
             <xsd:complexType>
               <xsd:sequence>
                 <xsd:element name="CPUData" maxOccurs="8">
                   <xsd:complexType>
                     <xsd:sequence>
                       <xsd:element name="Repetitions" type="xsd:string" />

                       <xsd:element name="Min">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="Max">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="Median">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="Mean">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="RDTSCDeltaViolation" minOccurs="0">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element ref="TestData" minOccurs="0" maxOccurs="1" />
                     </xsd:sequence>
                     <xsd:attribute name="CPUIndex" type="xsd:string"/>
                   </xsd:complexType>
                 </xsd:element>
               </xsd:sequence>
             </xsd:complexType>
          </xsd:element>  
      </xsd:sequence>

      <xsd:element name="CompletionStatus" type="CompletionStatusType"/>

    </xsd:sequence>                
  </xsd:complexType>
  
  <xsd:complexType name="CPUMPAssessmentType">  
    <xsd:sequence>
        <xsd:element name="OperationVersion" type="OperationVersionType" />
      <xsd:sequence minOccurs="0" maxOccurs="1">
          <xsd:element name="Units" type="UnitsType" minOccurs="3" maxOccurs="3"/>     
          <xsd:element name="NumThreads" type="xsd:string" />     
          <xsd:element name="WorkingBufferSize">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>
          <xsd:element name="TotalBytesPerSecond">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">              
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>     
          <xsd:element name="TotalBytesPerSecondMean">
            <xsd:complexType>
              <xsd:simpleContent>
                <xsd:extension base="xsd:string">              
                  <xsd:attribute name="units" /> 
                </xsd:extension>                
              </xsd:simpleContent>
            </xsd:complexType>
          </xsd:element>     
          <xsd:element ref="TestData" minOccurs="0" maxOccurs="1" />
          <xsd:element name="PerCPUData">
             <xsd:complexType>
               <xsd:sequence>
                 <xsd:element name="CPUData" maxOccurs="8">
                   <xsd:complexType>
                     <xsd:sequence>
                       <xsd:element name="Repetitions" type="xsd:string" />
                       <xsd:element name="Min">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     
                       <xsd:element name="Max">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     
                       <xsd:element name="Median">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     
                       <xsd:element name="Mean">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="StartTick">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                  <xsd:attribute name="microseconds" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="EndTick">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                  <xsd:attribute name="microseconds" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="Duration ">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                  <xsd:attribute name="microseconds" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element name="RDTSCDeltaViolation" minOccurs="0">
                           <xsd:complexType>
                              <xsd:simpleContent>
                                <xsd:extension base="xsd:string">              
                                  <xsd:attribute name="units" /> 
                                </xsd:extension>                
                              </xsd:simpleContent>
                           </xsd:complexType>
                       </xsd:element>     

                       <xsd:element ref="TestData" minOccurs="0" maxOccurs="1" />
                     </xsd:sequence>
                     <xsd:attribute name="CPUIndex" type="xsd:string"/>
                   </xsd:complexType>
                 </xsd:element>
               </xsd:sequence>
             </xsd:complexType>
          </xsd:element>  
      </xsd:sequence>

      <xsd:element name="CompletionStatus" type="CompletionStatusType"/>

      </xsd:sequence>                
  </xsd:complexType>

  <xsd:complexType name="DiskAssessmentType">  
    <xsd:sequence>
      <xsd:element name="OperationVersion" type="OperationVersionType" />
      <xsd:sequence minOccurs="0" maxOccurs="1">
      <xsd:element name="Units" type="UnitsType" minOccurs="3" maxOccurs="3"/>           
      </xsd:sequence>
      <xsd:element name="PerDiskData" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="DiskNumber" type="xsd:string"/>
            <xsd:element name="DiskSize" type="xsd:string"/>
            <xsd:element name="Zone" minOccurs="0" maxOccurs="unbounded">
              <xsd:complexType>
                <xsd:sequence>
                    <xsd:element name="ModeFlags">
                      <xsd:complexType>
                        <xsd:simpleContent>
                          <xsd:extension base="xsd:string">
                            <xsd:attribute name="friendlyName" />               
                          </xsd:extension>                
                        </xsd:simpleContent>
                      </xsd:complexType>
                    </xsd:element>
                    <xsd:element name="ZoneStart">
                        <xsd:complexType>
                            <xsd:simpleContent>
                              <xsd:extension base="xsd:string">              
                                <xsd:attribute name="units" /> 
                              </xsd:extension>                
                            </xsd:simpleContent>
                        </xsd:complexType>
                    </xsd:element>
                    <xsd:element name="ZoneEnd">
                        <xsd:complexType>
                            <xsd:simpleContent>
                              <xsd:extension base="xsd:string">              
                                <xsd:attribute name="units" /> 
                              </xsd:extension>                
                            </xsd:simpleContent>
                        </xsd:complexType>
                    </xsd:element>
                    <xsd:element name="Throughput">
                        <xsd:complexType>
                            <xsd:simpleContent>
                              <xsd:extension base="xsd:string">              
                                <xsd:attribute name="units" /> 
                              </xsd:extension>                
                            </xsd:simpleContent>
                        </xsd:complexType>
                    </xsd:element>                    
                    <xsd:element name="IssueTime">
                        <xsd:complexType>
                            <xsd:simpleContent>
                              <xsd:extension base="xsd:string">              
                                <xsd:attribute name="units" /> 
                              </xsd:extension>                
                            </xsd:simpleContent>
                        </xsd:complexType>
                    </xsd:element>                    
                    <xsd:element name="ETWData">
                      <xsd:complexType>
                         <xsd:sequence>
                            <xsd:element name="MinOffset">
                                <xsd:complexType>
                                    <xsd:simpleContent>
                                      <xsd:extension base="xsd:string">              
                                        <xsd:attribute name="units" /> 
                                      </xsd:extension>                
                                    </xsd:simpleContent>
                                </xsd:complexType>
                            </xsd:element>
                            <xsd:element name="MaxOffset">
                                <xsd:complexType>
                                    <xsd:simpleContent>
                                      <xsd:extension base="xsd:string">              
                                        <xsd:attribute name="units" /> 
                                      </xsd:extension>                
                                    </xsd:simpleContent>
                                </xsd:complexType>
                            </xsd:element>                            
                            <xsd:element name="AssessmentIOs">
                               <xsd:complexType>
                                 <xsd:sequence>                                                                     
                                    <xsd:element name="TotalData">
                                        <xsd:complexType>
                                            <xsd:simpleContent>
                                              <xsd:extension base="xsd:string">              
                                                <xsd:attribute name="units" /> 
                                              </xsd:extension>                
                                            </xsd:simpleContent>
                                        </xsd:complexType>
                                    </xsd:element>
                                    <xsd:element name="Count" type="xsd:string"/>                                                                
                                    <xsd:element name="ServiceTime">
                                      <xsd:complexType>
                                        <xsd:sequence>
                                          <xsd:element name="Total" type="xsd:string"/> 
                                          <xsd:element name="Average" type="xsd:string"/>
                                          <xsd:element name="InterferenceCount" type="xsd:string"/>
                                          <xsd:element name="InterferenceCountWithReads" type="xsd:string"/>
                                        </xsd:sequence>
                                        <xsd:attribute name="units"/>
                                      </xsd:complexType>
                                    </xsd:element>
                                    <xsd:element name="IOTime">
                                      <xsd:complexType>
                                        <xsd:sequence>
                                          <xsd:element name="Total" type="xsd:string"/> 
                                          <xsd:element name="Average" type="xsd:string"/> 
                                        </xsd:sequence>
                                        <xsd:attribute name="units"/>
                                      </xsd:complexType>
                                    </xsd:element>
                                    <xsd:element name="AvgIOTimeToSrvTimeDelta">
                                        <xsd:complexType>
                                            <xsd:simpleContent>
                                              <xsd:extension base="xsd:string">              
                                                <xsd:attribute name="units" /> 
                                              </xsd:extension>                
                                            </xsd:simpleContent>
                                        </xsd:complexType>
                                    </xsd:element>                                    
                                 </xsd:sequence>
                               </xsd:complexType>
                            </xsd:element>
                            <xsd:element name="NonAssessmentIOs">
                              <xsd:complexType>
                                <xsd:sequence>
                                  <xsd:element name="Reads">
                                    <xsd:complexType>
                                      <xsd:sequence>
                                        <xsd:element name="TotalData">
                                          <xsd:complexType>
                                              <xsd:simpleContent>
                                                <xsd:extension base="xsd:string">              
                                                  <xsd:attribute name="units" /> 
                                                </xsd:extension>                
                                              </xsd:simpleContent>                                              
                                          </xsd:complexType>
                                        </xsd:element>
                                        <xsd:element name="Count" type="xsd:string"/> 
                                      </xsd:sequence>
                                    </xsd:complexType>
                                  </xsd:element>
                                  <xsd:element name="Writes">
                                    <xsd:complexType>
                                      <xsd:sequence>
                                        <xsd:element name="TotalData">
                                          <xsd:complexType>
                                              <xsd:simpleContent>
                                                <xsd:extension base="xsd:string">              
                                                  <xsd:attribute name="units" /> 
                                                </xsd:extension>                
                                              </xsd:simpleContent>                                              
                                          </xsd:complexType>
                                        </xsd:element>
                                        <xsd:element name="Count" type="xsd:string"/> 
                                      </xsd:sequence>
                                    </xsd:complexType>
                                  </xsd:element>
                                </xsd:sequence>
                              </xsd:complexType>
                            </xsd:element>
                            <xsd:element name="Throughput" type="xsd:string"/>                                                                                   
                         </xsd:sequence>
                      </xsd:complexType>
                    </xsd:element>
                    <xsd:element name="FlushProfile" minOccurs="0">
                      <xsd:complexType>
                        <xsd:sequence>
                          <xsd:element name="Score" type="xsd:string" />
                          <xsd:element name="ReadOnlyStats" type="EvalStatsType" />
                          <xsd:element name="WriteOnlyStats" type="EvalStatsType" />
                          <xsd:element name="FlushDurationUs" type="xsd:string" />
                          <xsd:element name="ReadWithSeqWriteStats">
                            <xsd:complexType>
                              <xsd:sequence>
                                <xsd:element name="Read" type="EvalStatsType" />
                                <xsd:element name="Write" type="EvalStatsType" />
                                <xsd:element name="Flush" type="EvalStatsType" />
                              </xsd:sequence>
                            </xsd:complexType>
                          </xsd:element>
                          <xsd:element name="ReadWithRandWriteStats">
                            <xsd:complexType>
                              <xsd:sequence>
                                <xsd:element name="Read" type="EvalStatsType" />
                                <xsd:element name="Write" type="EvalStatsType" />
                                <xsd:element name="Flush" type="EvalStatsType" />
                              </xsd:sequence>
                            </xsd:complexType>
                          </xsd:element>                          
                          <xsd:element name="ReadTimeWithSeqWrites" type="xsd:string" />
                          <xsd:element name="ReadWriteTimeWithSeqWrites" type="xsd:string" />
                          <xsd:element name="DiskTimeWithSeqWrites" type="xsd:string" />
                          <xsd:element name="ReadTimeWithRandWrites" type="xsd:string" />
                          <xsd:element name="ReadWriteTimeWithRandWrites" type="xsd:string" />
                          <xsd:element name="DiskTimeWithRandWrites" type="xsd:string" />
                        </xsd:sequence>
                      </xsd:complexType>
                    </xsd:element>
                  <xsd:element name="Interference" minOccurs="0" />
                  <xsd:element name="IOData" minOccurs="0" maxOccurs="unbounded">
                    <xsd:complexType>
                      <xsd:attribute name="IOType" />
                      <xsd:attribute name="SrvTime" />
                      <xsd:attribute name="fileOffset" />
                      <xsd:attribute name="SizeBytes" />
                      <xsd:attribute name="PreceededWithAsmIO" />                      
                    </xsd:complexType>
                  </xsd:element>
                </xsd:sequence>
              </xsd:complexType>
            </xsd:element>                        
            </xsd:sequence>
        </xsd:complexType>
      </xsd:element>            

      <xsd:element name="CompletionStatus" type="CompletionStatusType"/>

      </xsd:sequence>                
  </xsd:complexType>

  <xsd:complexType name="EvalStatsType">
    <xsd:sequence>
      <xsd:element name="Count" type="xsd:string"/>
      <xsd:element name="TotalBytes" type="xsd:string"/>
      <xsd:element name="Median" type="xsd:string"/>
      <xsd:element name="Mean" type="xsd:string"/>
      <xsd:element name="StdDev" type="xsd:string"/>
    </xsd:sequence>
  </xsd:complexType>
    
  <xsd:complexType name="D3DGraphicsType">
    <xsd:sequence>
      <xsd:element name="OperationVersion" type="OperationVersionType" />
      <xsd:element name="Results"  minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="CmdLine" type="xsd:string" minOccurs="0"/>               
            <xsd:element name="EffectiveFPS" type="xsd:string" />
            <xsd:element name="Valid" type="xsd:string" />
            <xsd:element name="HRESULT" type="xsd:string" />
            <xsd:element name="FPS" type="xsd:string" />
            <xsd:element name="Idle" type="xsd:string" />
            <xsd:element name="FramesRendered" type="xsd:string" />
            <xsd:element name="AverageFrameTimeMS" type="xsd:string" />
            <xsd:element name="StDevFrameTimeMS" type="xsd:string" />
            <xsd:element name="Duration" type="xsd:string" />
            <xsd:element name="StartTime" type="xsd:string" />
            <xsd:element name="EndTime" type="xsd:string" />
            <xsd:element name="Frequency" type="xsd:string" />
            <xsd:element name="WDDMFps" type="xsd:string" />
                  <xsd:element name="WDDMMbVideoMemPerSecond" type="xsd:string" />
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>
      <xsd:element name="CompletionStatus" type="CompletionStatusType"/>
    </xsd:sequence>
    <xsd:attribute name="AssessmentName" type="xsd:string" />
  </xsd:complexType>

  <xsd:complexType name="DWMGraphicsType">
          <xsd:sequence>
            <xsd:element name="OperationVersion" type="OperationVersionType" />
            <xsd:element name="Results"  minOccurs="0">
              <xsd:complexType>
                <xsd:sequence>
                  <xsd:element name="CmdLine" type="xsd:string" minOccurs="0"/>               
                 <xsd:element name="EffectiveFPS" type="xsd:string" />
                  <xsd:element name="Valid" type="xsd:string" />
                  <xsd:element name="HRESULT" type="xsd:string" />
                  <xsd:element name="FPS" type="xsd:string" />
                  <xsd:element name="Idle" type="xsd:string" />
                  <xsd:element name="FramesRendered" type="xsd:string" />
                  <xsd:element name="AverageFrameTimeMS" type="xsd:string" />
                  <xsd:element name="StDevFrameTimeMS" type="xsd:string" />
                  <xsd:element name="Duration" type="xsd:string" />
                  <xsd:element name="MbVideoMemPerSecond" type="xsd:string" />
                  <xsd:element name="StartTime" type="xsd:string" />
                  <xsd:element name="EndTime" type="xsd:string" />
                  <xsd:element name="Frequency" type="xsd:string" />
                  <xsd:element name="WDDMFps" type="xsd:string" />
                  <xsd:element name="WDDMMbVideoMemPerSecond" type="xsd:string" />
                </xsd:sequence>
              </xsd:complexType>
            </xsd:element>
            <xsd:element name="CompletionStatus" type="CompletionStatusType"/>
          </xsd:sequence>
    <xsd:attribute name="AssessmentName" type="xsd:string" />
  </xsd:complexType>

  <xsd:complexType name="GraphicsResultGroupType">
    <xsd:sequence minOccurs="0" maxOccurs="unbounded">
      <xsd:choice>
        <xsd:element name="DWMAssessment" type="DWMGraphicsType" />
        <xsd:element name="D3DAssessment" type="D3DGraphicsType" />
      </xsd:choice>
      <xsd:element ref="AssessmentRunTime" />
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="MediaEncodeType">
    <xsd:sequence>
      <xsd:element name="OperationVersion" type="OperationVersionType" />
      <xsd:element name="Results" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="TotalTime" type="xsd:string" />
            <xsd:element name="UserTime" type="xsd:string" />
            <xsd:element name="IsrDpcTime" type="xsd:string" />
            <xsd:element name="LongestThread" type="xsd:string" />
            <xsd:element name="Priority" type="xsd:string" />
            <xsd:element name="TimedOut" type="xsd:string" />
            <xsd:element name="HRESULT" type="xsd:string" />
              <xsd:element name="Encode" type="MediaAssessmentEncodeDetailType"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="CompletionStatus" type="CompletionStatusType"/>

      </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="MediaDecodeType">
    <xsd:sequence>
      <xsd:element name="OperationVersion" type="OperationVersionType" />
      <xsd:element name="Results" minOccurs="0">
        <xsd:complexType>
          <xsd:sequence>
            <xsd:element name="TotalTime" type="xsd:string" />
            <xsd:element name="UserTime" type="xsd:string" />
            <xsd:element name="IsrDpcTime" type="xsd:string" />
            <xsd:element name="LongestThread" type="xsd:string" />
            <xsd:element name="Priority" type="xsd:string" />
            <xsd:element name="TimedOut" type="xsd:string" />
            <xsd:element name="HRESULT" type="xsd:string" />
            <xsd:element name="Playback" type="MediaAssessmentPlaybackDetailType"/>
          </xsd:sequence>
        </xsd:complexType>
      </xsd:element>

      <xsd:element name="CompletionStatus" type="CompletionStatusType"/>

      </xsd:sequence>
  </xsd:complexType>

   <xsd:complexType name="MediaAssessmentPlaybackDetailType">
    <xsd:sequence>
       <xsd:element name="FrameCount" type="xsd:string" />
       <xsd:element name="MinFrame" type="xsd:string" />
       <xsd:element name="FirstQFrame" type="xsd:string" />
       <xsd:element name="ThirdQFrame" type="xsd:string" />
       <xsd:element name="MaxFrame" type="xsd:string" />
       <xsd:element name="Mean" type="xsd:string" />
       <xsd:element name="Median" type="xsd:string" />
       <xsd:element name="IQR" type="xsd:string" />
    </xsd:sequence>
  </xsd:complexType>

  <xsd:complexType name="MediaAssessmentEncodeDetailType">
    <xsd:sequence>
      <xsd:element name="NYI" type="xsd:string" />
    </xsd:sequence>
  </xsd:complexType>

 <xsd:complexType name="CompletionStatusType">
         <xsd:simpleContent>
            <xsd:extension base="xsd:string">              
                <xsd:attribute name="description" /> 
            </xsd:extension>                
         </xsd:simpleContent>
  </xsd:complexType>

</xsd:schema>
```



 

 




