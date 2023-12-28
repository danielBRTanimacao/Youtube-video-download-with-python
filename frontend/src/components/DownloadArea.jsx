import { useState } from "react";

import VideoDownloads from "./VideoDownloads.jsx";

export default () => {
    const [linkTxt, setLink] = useState("");

    const [ytError, setYtError] = useState(true);

    function cathLink() {
        let txtlink = document.querySelector("#linkCather").value;
        const ytRegex =
            /^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$/;
        if (ytRegex.test(txtlink)) {
            setLink(txtlink);
        } else {
            setYtError(false);
        }
    }

    return (
        <>
            <section className="bg-yt">
                <div className="p-5 container text-center">
                    <div className="d-flex justify-content-center">
                        <h1 className="me-2 pt-1">Insira um link e baixe</h1>
                        <h1 className="display-4 fs-bowb color-primary txt-deco no-under">
                            qualquer tipo de vídeo!
                        </h1>
                    </div>
                    <div className=" row">
                        <div className="pt-5 pb-3">
                            <input
                                type="text"
                                className="form-control form-control-lg col-md-6 shadow"
                                placeholder="link..."
                                id="linkCather"
                            />
                            <button
                                className="btn btn-lg btn-primary col-md-6 mt-3"
                                onClick={cathLink}
                            >
                                enviar
                            </button>
                        </div>
                    </div>
                </div>
            </section>
            <VideoDownloads link={linkTxt} ytValid={ytError} />
        </>
    );
};
