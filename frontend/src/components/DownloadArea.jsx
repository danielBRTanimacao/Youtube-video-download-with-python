import { useState } from "react";
import validateYtLink from "../assets/js/ValidateYtLink";

export default () => {
    const [link, setLink] = useState();

    const videoSubmited = () => {
        validateYtLink(link);
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
                                onClick={videoSubmited}
                            >
                                enviar
                            </button>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
};
