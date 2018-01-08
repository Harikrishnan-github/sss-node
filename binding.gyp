{
  "targets": [
    {
      "target_name": "shamirsecretsharing",
      "cflags": ["-g", "-Wall", "-march=native", "-Wno-sign-compare"],
      "cflags_cc": ["-g", "-Wall", "-march=native", "-fexceptions"],
      "sources": [
        "shamirsecretsharing.cc",
        "sss/randombytes/randombytes.c",
        "sss/sss.c",
        "sss/hazmat.c",
        "sss/tweetnacl.c"
      ],
      "include_dirs" : [
        "sss",
        "sss/randombytes",
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ["OS==\"mac\"", {
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
          }
        }]
      ]
    }
  ]
}
