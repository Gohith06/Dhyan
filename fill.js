fields =["duration",
"protocol_type",
"service",
"flag",
"src_bytes",
"dst_bytes",
"land",
"wrong_fragment",
"urgent",
"hot",
"num_failed_logins",
"logged_in",
"num_compromised",
"root_shell",
"su_attempted",
"num_root",
"num_file_creations",
"num_shells",
"num_access_files",
"num_outbound_cmds",
"is_host_login",
"is_guest_login",
"count",
"srv_count",
"serror_rate",
"srv_serror_rate",
"rerror_rate",
"srv_rerror_rate",
"same_srv_rate",
"diff_srv_rate",
"srv_diff_host_rate",
"dst_host_count",
"dst_host_srv_count",
"dst_host_same_srv_rate",
"dst_host_diff_srv_rate",
"dst_host_same_src_port_rate",
"dst_host_srv_diff_host_rate",
"dst_host_serror_rate",
"dst_host_srv_serror_rate",
"dst_host_rerror_rate",
"dst_host_srv_rerror_rate",
"level"]

function fill(s){
    obj = {}
    s = s.split(",")
    l = s.length
    for(let i=0;i<l;i++){
        obj[fields[i]] = [s[i]];
    }
    return obj
}

const post = async (obj)=>{
    const res = await fetch("http://127.0.0.1:5000/predict",{
        method:"POST",
        headers:{
            "content-type":"application/json"
        },
        body: JSON.stringify(obj),
    })
    const data = await res.json()
    console.log(data)
}

const send = (s) =>{
    post(fill(s))
}

const sendAll = (f)=>{
    f.split("\n").forEach(s=>{
        send(s)
    })
}

sendAllEncode(){
    

}