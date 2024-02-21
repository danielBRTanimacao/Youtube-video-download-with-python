import { useState } from "react";
import ReactPlayer from "react-player";
import validateYtLink from "../assets/js/ValidateYtLink";

import TableRender from "./TableRender";

export default () => {
    const [link, setLink] = useState("");
    const [showDiv, setShowDiv] = useState(true);

    const videoSubmited = () => {
        if (validateYtLink(link)) setShowDiv(false);
    };

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
                    {showDiv ? (
                        <div className="row">
                            <div className="pt-5 pb-3">
                                <input
                                    onChange={(e) => setLink(e.target.value)}
                                    type="text"
                                    className="form-control form-control-lg col-md-6 shadow"
                                    placeholder="link..."
                                    required
                                />
                                <button
                                    type="submit"
                                    className="btn btn-lg btn-primary col-md-6 mt-3"
                                    id="btn-for-submit"
                                    onClick={videoSubmited}
                                >
                                    enviar
                                </button>
                            </div>
                        </div>
                    ) : (
                        <div className="row">
                            <h1 className="my-3">Este e o seu vídeo?</h1>
                            <div className="d-flex justify-content-center">
                                <ReactPlayer url={link} />
                            </div>
                            <div className="mt-4">
                                <TableRender />
                            </div>
                        </div>
                    )}
                </div>
            </section>
        </>
    );
};
