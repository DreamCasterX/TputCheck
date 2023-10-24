# Copyright (c) 2006 Red Hat, Inc. All rights reserved. This copyrighted material
# is made available to anyone wishing to use, modify, copy, or
# redistribute it subject to the terms and conditions of the GNU General
# Public License v.2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# Author: Greg Nichols
#
# xml tags for rhcert


class Tags:
    certification_test="certification-test"
    certification="certification"
    type="type"
    os="os"
    release="release"
    update="update"
    kernel="kernel"
    name="name"
    version="version"
    hardware="hardware"
    model="model"
    make="make"
    vendor="vendor"
    arch="arch"
    test="test"
    hal="hal"
    udisks="udisks"
    system="system"
    output="output"
    summary="summary"
    run="run"
    test_server = "test-server"
    device = "device"
    property="property"
    hostname="hostname"
    rhcert_environment="rhcert-environment"
    rhcert_task="rhcert-task"
    file_system="file-system"
    data_directory="data-directory"
    server_directory="server-directory"
    suite_directory="suite-directory"
    store_directory="store-directory"
    library_directory="library-directory"
    log_directory="log-directory"
    device_class="device-class"
    attachment="attachment"
    guest_config_directory="guest-config-directory"
    kvm_guest_config_directory="kvm-guest-config-directory"
    guest_image_directory="guest-image-directory"
    kvm_guest_image_directory="kvm-guest-image-directory"
    kvm_guest_nvram_directory="kvm-guest-nvram-directory"
    guest_boot_directory="guest-boot-directory"
    fv_image_mountpoint="fv-image-mountpoint"
    fv_image_repo_directory="fv-image-repo-directory"
    urls="urls"
    url="url"
    os_type="os_type"
    agent="agent"
    subtest="subtest"
    tag="tag"
    image="image"
    host="host"
    rhcert_image="rhcert-image"
    time_limits="time-limits"
    rhcert_kernel_info="rhcert-kernel-info"
    product_url="product-url"
    support_url = "support-url"
    specification_url = "specification-url"
    catalog_url="catalog-url"
    bugzilla_url="bugzilla-url"
    services_url="services-url"
    category="category"
    parameters="parameters"
    server="server"
    email="email"
    product="product"
    suite="suite"
    package="package"
    ftp_dropbox_upload="ftp-dropbox-upload"
    ftp_dropbox_download="ftp-dropbox-download"
    description="description"
    public_key="public-key"
    ip_address="ip-address"
    connection="connection"
    log="log"
    vendor_products="vendor-products"
    program="program"
    baseRHEL="baseRHEL"
    plan_component="plan-component"
    proxy_url="proxy-url"
    deferred="deferred"
    container_projects = "container_projects"
    container_project = "container_project"
    certified_containers = "certified_containers"
    certified_container = "certified_container"
    image_SHAs = "image-SHAs"
    image_SHA = "image-SHA"
    headers="headers"
    payload="payload"
    pass_though_product="pass-through-product"
    command="command"
    regex="regex"
    stdout="stdout"
    stderr="stderr"
    role="role"
    server_settings="server-settings"
    feature="feature"
    feature_item="feature-item"
    versions="versions"
    host_role="host-role"
    node="node"


class Attributes:
    rhcert_version="rhcert-version"
    rhcert_release="rhcert-release"
    name="name"
    md5sum="md5sum"
    mime_type="mime-type"
    encoding="encoding"
    udi="udi"
    label="label"
    return_value="return-value"
    discover_time="discover-time"
    plan_time="plan-time"
    run_time="run-time"
    end_time="end-time"
    number="number"
    number_of_runs="number-of-runs"
    mode="mode"
    device_class="device-class"
    logical_device="logical-device"
    device_bus="device-bus"
    interactive="interactive"
    source="source"
    test_server = "test-server"
    lock_file = "lock-file"
    database_name = "database-name"
    mandatory = "mandatory"
    status="status"
    product="product"
    function="function"
    task_file="task_file"
    maximum_sos_plugin_size="maximum-sos-plugin-size"
    maximum_attachment_size="maximum-attachment-size"
    maximum_dialog_attachment_size="maximum-dialog-attachment-size"
    description="description"
    type="type"
    type_id="type-id"
    user="user"
    password="password"
    priority="priority"
    time="time"
    results_warning_size="results-warning-size"
    fv_guest_timelimit="fv-guest-timelimit"
    reboot_timelimit="reboot-timelimit"
    ssh_retry_timeout = "ssh-retry-timeout"
    export="export"
    transfer="transfer"
    kernel="kernel"
    certification_name="certification-name"
    id="id"
    catalog_url="catalog-url"
    from_address="from-address"
    smtp_host="smtp-host"
    specification_id="specification-id"
    search_timeout="search-timeout"
    search_retries="search-retries"
    path="path"
    source_directory="source-directory"
    major="major"
    minor="minor"
    minor_max="minor-max"
    minor_min="minor-min"
    short_name="short-name"
    task="task"
    listener_port="listener-port"
    certification_id="certification_id"
    upload_time="upload-time"
    submit_time="download-time"
    state="state"
    authentication="authentication"
    workflow="workflow"
    installed="installed"
    ip_address="ip-address"
    use="use"
    port="port"
    container="container"
    protocol="protocol"
    role="role"
    scratch_id="scratch-id"
    ecosystem="ecosystem"
    idref="idref"
    minor_version_policy="minor-version-policy"
    bug_id="bug-id"
    is_supplemental="is-supplemental"
    component="component"
    component_id="component-id"
    node_id="node_id"
    product_version="product-version"
    full_version="full-version"
    vendor="vendor"
    bits="bits"
    dialog_order="dialog-order"
    key="key"
    ci_timelimit="ci-timelimit"
    ci_poll="ci-poll"
    validation_job_id="validation-job-id"
    sandbox="sandbox"
    url="url"
    data_value="data-value"
    openstack_specific="openstack_specific"
    maximum_microversion="maximum_microversion"
    platform="platform"
    created='created'
    updated='updated'
    version="version"
    sync="sync"
    sync_time="sync-time"
    sync_range="sync-range"
    category="category"
    test_plan_status="test-plan-status"
    test_id="test-id"
    phase="phase"
    leveraged_test_id="leveraged-test-id"
    leveraged_cert_id="leveraged-cert-id"
    base_product_id="base-product-id"
    configuration="configuration"
    pass_through_vendor="pass-through-vendor"
    command="command"
    group = "group"
    single_line = "single-line"
    signal = "signal"
    public = "public"
    multihost_run_time = "multihost-run-time"
    image_SHAs = "image-SHAs"
    multistore_enabled = "multistore-enabled"
    database_path = "database-path"
    image_id = "image-id"
    iperf_port = "iperf-port"
    total_iperf_ports = "total-iperf-ports"
    hostname = "hostname"
    project_id = "project-id"
    image = "image"
    api_key = "api-key"
    preflight = "preflight"
    unit_file = "unit-file"
    claim = "claim"
    results = "results"
    nfs_port = "nfs-port"
    nodes = "nodes"
    nodesHwInfo = "nodesHwInfo"
    Lscpu = "Lscpu"
    lscpu = "lscpu"
    Lspci="Lspci"
    field = "field"
    data = "data"

class Constants:
    PASS="PASS"
    FAIL="FAIL"
    WARN="WARN"
    REVIEW="REVIEW"
    ABORT="ABORT"
    DISABLED="DISABLED"
    ENABLED="ENABLED"
    INCOMPLETE="INCOMPLETE"
    DATETIMEFORMAT="%Y-%m-%d %H:%M:%S"
    UTCDATETIMEFORMAT="%Y%m%dT%H:%M:%S"
    UTCDATETIMEFORMATZ="%Y-%m-%dT%H:%M:%SZ" # new hydra-cwe apis use this format

    # Products IDs from PNS
    RHEL_PROD_ID = 1
    RHELMRG_PROD_ID = 10
    RHEL4ARM_PROD_ID = 7
    RHELforPower_PROD_ID = 9
    RHELRT_PROD_ID = 6

    TRUE="true"
    FALSE="false"
    yes="yes"
    no="no"
    outputfile="outputfile"
    runmode="runmode"
    testserver="testserver"
    source="source"
    plan = "plan"
    summary = "summary"
    full = "full"
    normal = "normal"
    auto = "auto"
    self = "self"
    forced = "forced"
    ALL = "ALL"
    hal = "hal"
    udisks="udisks"
    proc = "proc"
    user = "user"
    username = "username"
    device = "device"
    OSCommand = "OSCommand"
    FunctionKey = "FunctionKey"
    memory =  "mem"
    disk = "disk"
    freeze = "freeze"
    rhcertserverstatus = "rhcertserverstatus"
    hwCertServerMinimumVersion = "7.1"
    running = "running"
    failed = "failed"
    HwCert = "HwCert"
    rhcert = "rhcert"
    rhcert_util = "rhcert-util"
    rhcert_cli = "rhcert-cli"
    rhcertd = "rhcertd"
    off = "off"
    low = "low"
    medium = "medium"
    high = "high"
    pre = "pre"
    post = "post"
    disabled="disabled"
    deleted="deleted"
    paravirtualization="paravirtualization"
    fullvirtualization="fullvirtualization"
    manual="manual"
    RHTS="RHTS"
    udev="udev"
    udi = "udi"
    info_dot_udi="info.udi"
    kvm="kvm"
    xen="xen"
    hvm="hvm"
    rt="rt"
    TAINT_PROPRIETARY_MODULE = 1
    TAINT_UNSIGNED_MODULE = 64   #kernel.h calls this TAINT_USER?
    TAINT_TECHPREVIEW_MODULE = 1 << 29
    i386="i386"
    i686="i686"
    s390="s390"
    s390x="s390x"
    x86_64="x86_64"
    ppc64le="ppc64le"
    aarch64="aarch64"
    ia64="ia64"
    interactive="interactive"
    noninteractive="noninteractive"
    certification="certification"
    sandbox = "sandbox"
    osqa="osqa"
    DEBUG="DEBUG"
    debug="debug"
    reboot="reboot"
    panic="panic"
    local="local"
    nfs="nfs"
    rcp="rcp"
    results="results"
    html="html"
    text="text"
    junit="junit"
    all="all"
    clean="clean"
    kudzu="kudzu" # still needed due to parsing fv results from RHEL5 guests
    log="log"
    serverNVRRegex="%s[^0-9]+(?P<version>[\.0-9]+)[^0-9]+(?P<release>[0-9]+)" % rhcert
    # Bytes per
    TB = 1099511627776
    GB = 1073741824
    MB = 1048576
    KB = 1024
    id = "id"
    bus = "bus"
    major_version = "major-version"
    minor_version = "minor-version"
    product = "product"
    status = "status"
    dbus = "dbus"
    store = "store"
    systems = "systems"
    transfer = "transfer"
    rhcert_transfer = "rhcert-transfer"
    server = "server"
    install = "install"
    closed = "closed"
    fv_images = "fv-images"
    runs = "runs"
    RedHatInc = "Red Hat, Inc."
    cwe = "cwe"
    bz = "bz"
    exact = "exact"
    minimum = "minimum"
    maximum = "maximum"
    newest = "newest"
    oldest = "oldest"
    sso = "sso"
    certification_label="Red Hat Hardware Certification test"
    Red_Hat_Enterprise_Linux="Red Hat Enterprise Linux"
    RHOSP = "RHOSP"
    locale = "en_US.UTF-8"
    utf_8 = "utf-8"
    unicode = "unicode"
    before_pxe = "before-pxe"
    after_pxe = "after-pxe"
    maximumResultsFileNameLength = 80 # limit imposed by hydra's use of SFDC
    rhcert_hosted_on_host = "rhcert.connect.redhat.com"
    cinder_lib = "cinder_lib"
    NFS_protocol = "NFS"
    Red_Hat_Gold_Image = "Red Hat Gold Image"
    genuine_intel = "GenuineIntel"
    authentic_amd = "AuthenticAMD"
    managementSyncRange = 45 # days default certification listing
    storage_test = "storage-test"
    rdma_test = "rdma-test"
    rdma_device = "rdma-device"
    network_test = "network-test"
    network_device = "network-device"
    pci_id = "pci-id"
    pci_subsys_id = "pci-subsys-id"
    device_description = "device-description"
    provision = "provision"
    run = "run"
    save = "save"
    #Iconic drivers
    ironic_driver = "ironic-driver"
    page4kilobytes = 4096  # 4k page size
    page64kilobytes = 65536  # 64k page size
    Internal = "Internal"
    passed = "passed"
    skipped = "skipped"
    kernel_debuginfo = "kernel-debuginfo"
    kernel_64K_debuginfo = "kernel-64k-debuginfo"
    kernel_rt_debuginfo = "kernel-rt-debuginfo"
    kernel_rt_debuginfo_common = "kernel-rt-debuginfo-common"
    clusterID = "clusterID"
    platform = "platform"
    type="type"
    base_dns_domain="base_dns_domain"
    api_vip_dns_name="api_vip_dns_name"
    loopbackIP4 = "127.0.0.1"
    auth = "auth"
    dnf = "dnf"
    yum = "yum"
    tick_symbol = "\u2713"
    DAEMON_START = "DAEMON_START"
    SOFTWARE_UPDATE = "SOFTWARE_UPDATE"

class VersionType:
    release = "release"
    candidate = "candidate"
    update = "update"


class Paths:
    openstack_config_path = "/etc/redhat-certification/openstack"


class SystemFunction:
    system = "system"
    storage = "storage"
    networking = "networking"
    human_interface = "human-interface"


class DeviceClass:
    system = "system"
    processor = "processor"
    memory = "memory"
    battery = "battery"
    usb = "usb"
    pccard = "pccard"
    expresscard = "expresscard"
    hard_disk = "hard-disk"
    optical = "optical"
    sequential = "sequential"
    floppy = "floppy"
    network_interface = "network-interface"
    display = "display"
    audio = "audio"
    input = "input"


class DeviceNumberMajor:
    floppyBlock = 2
    ideBlock = 3
    scsiBlock = 8
    raidBlock = 9


class PCIDeviceClass:
    massStorage = 1


class TestTag:
    interactive = "interactive"
    auto_support = "auto-support"
    noninteractive = "non-interactive"
    certification = "certification"
    osqa = "osqa"
    portable = "portable"
    virtualization="virtualization"
    realtime="realtime"
    network="network"
    usb="usb"
    wlan="wlan"
    neutron="neutron"
    cinder="cinder"
    manila="manila"
    storage="storage"
    baremetal="baremetal"
    profiler="profiler"
    rdma = "rdma"
    infiniband = "infiniband"
    omnipath = "omnipath"
    roce = "roce"
    designate = "designate"
    iwarp = "iwarp"
    memory = "memory"

    @staticmethod
    def getAll():
        tags = list()
        for key in vars(TestTag):
            if "_" not in key and "getAll" not in key:
                tags.append(vars(TestTag)[key])
        return tags


class RHEL:

    # Wrapper function for the lazy import of the rhcert.version module,
    # which may or may not exist when the tags.py module is first imported.
    def __major():
        __rhel_version = 'unknown'

        try:
            from rhcert.version import rhel_version
        except ImportError as e:
            pass
        else:
            __rhel_version = "RHEL{0}".format(rhel_version)

        return __rhel_version

    major = __major()


class Programs:
    """ This class represents the "packaged" programs, that is,
    the programs with test suites packaged in rpm as redhat-certification-<program> """

    # hwcert/tests/info/info.py +30, KernelTest.__init__(self, "hwcert/info")
    # suitename passes as hwcert. Adding it for short term, will figure out
    # some other solution later.
    _hardware =  "hwcert"
    hardware = "hardware"
    software = "software"
    container = "container"
    automotive = "automotive"
    # Ironic certification
    baremetal = "baremetal"
    openstack = "openstack"
    cloud = "cloud"
    cloud_sap = "cloud-sap"
    openshift = "openshift"

    @staticmethod
    def getAllPackaged():
        tags = list()
        for key in vars(Programs):
            if "__" not in key and key not in ["getAllPackaged", "ecosystems", "_hardware"]:
                tags.append(vars(Programs)[key])
        return tags


class States:
    new = "new"
    open = "open"
    retest = "retest"
    certify = "certify"
    recertify = "recertify"

    @staticmethod
    def getAll():
        tags = list()
        for key in vars(States):
            if "_" not in key and "getAll" not in key:
                tags.append(vars(States)[key])
        return tags


class Sync:
    idle = "idle"
    running = "running"
    reset = "reset"


class ServerConfiguration:
    default = "default"
    management = "management"
    testing = "testing"
    notInstalled = 'notInstalled'


class Operations:
    new_system = "new-system"
    remove = "remove"
    restart = "restart"
    toggle_debug = "toggle-debug"
    reset_sync = "reset-sync"
    dialog = "dialog"
    open_ports = "open-ports"

    @staticmethod
    def getAll():
        tags = list()
        for key in vars(Operations):
            if "__" not in key and "getAll" not in key:
                tags.append(vars(Operations)[key])
        return tags

class HostRole:
    """ Note: not all host roles are static/hard-coded """
    test_server = "test-server"
    sut = "sut"
    compute = "compute"
    controller = "controller"

    @staticmethod
    def getAll():
        roles = list()
        for key in vars(HostRole):
            if "_" not in key and "getAll" not in key:
                roles.append(vars(States)[key])
        return roles

    @staticmethod
    def parse(hostRoles):
        # parse a list of host options such as ["controller:192.168.1.20", "compute:192.168.1.43"]
        # return a dict such as {"controller": "192.168.1.20", "compute": "192.168.1.43"}
        hostDictionary = {}
        for host in hostRoles:
            values = host.split(':', 1)
            hostDictionary[values[0]] =  values[1]
        return hostDictionary

# Wrapper function for the lazy import of the rhcert.version module,
# which may or may not exist when the tags.py module is first imported.
def __getVersionRelease():
    try:
        from rhcert.version import version as rhcert_version
        from rhcert.version import release as rhcert_release
    except ImportError as e:
        return 'unknown, unknown'

    return rhcert_version, rhcert_release

class Regex: # important regex's for rhcert
    # hostname could be ip address
    resultsFileName = "^rhcert-results-(?P<hostname>.+)-(?P<date>[0-9]+)\.xml(.gz)?$"
    multiHostFileName = "^rhcert-multi-(?P<program>.+)-(?P<certID>.+)-(?P<date>[0-9]+)\.xml(.gz)?$"

def unitTest():

    rhcert_version, rhcert_release = __getVersionRelease()
    print("rhcert version: %s build %s" % (rhcert_version, rhcert_release))
    print("TestTags:")
    for tag in TestTag.getAll():
        print(tag)
    print("")
    print("Packaged Programs:")
    for tag in Programs.getAllPackaged():
        print(tag)
    print("")
    print("States:")
    for tag in States.getAll():
        print(tag)
    print("")

    return True

if __name__ == "__main__":
    if not unitTest():
        print("tags.py unit test FAILED")
        exit(1)
    print("tags.py unit test passed")
    exit(0)
